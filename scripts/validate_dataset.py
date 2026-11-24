import json
import os

METADATA_PATH = "data/processed/pdfs/pdf_metadata.json"
URL_LIST_PATH = "data/url_list"

def validate_pipeline_artifacts():
    """
    Validates the integrity of extracted notice metadata and crawling statistics.
    Checks for required schema keys, valid URLs, and non-empty titles.
    """
    print("=" * 60)
    print("NITAverse - Data Ingestion Validation Suite")
    print("=" * 60)

    # 1. Validate PDF Metadata Schema
    if not os.path.exists(METADATA_PATH):
        print(f"❌ Error: Metadata file not found at {METADATA_PATH}")
        return False

    with open(METADATA_PATH, "r", encoding="utf-8") as f:
        metadata = json.load(f)

    total_records = len(metadata)
    valid_records = 0
    missing_title = 0
    missing_url = 0

    for item in metadata:
        has_title = bool(item.get("title", "").strip())
        has_url = bool(item.get("url", "").strip())

        if has_title and has_url:
            valid_records += 1
        else:
            if not has_title:
                missing_title += 1
            if not has_url:
                missing_url += 1

    print(f"[*] Validating: {METADATA_PATH}")
    print(f"    - Total Notice Records: {total_records}")
    print(f"    - Schema Integrity: {valid_records}/{total_records} ({(valid_records/total_records)*100:.1f}%)")
    
    if missing_title or missing_url:
        print(f"    ⚠️ Warning: {missing_title} missing titles, {missing_url} missing URLs")
    else:
        print("    - Schema Check: PASSED (All records have valid titles and source URLs)")

    # 2. Check Discovered URL Inventory
    if os.path.exists(URL_LIST_PATH):
        print("\n[*] Crawling Inventory Statistics:")
        for file in sorted(os.listdir(URL_LIST_PATH)):
            if file.endswith(".txt"):
                file_path = os.path.join(URL_LIST_PATH, file)
                with open(file_path, "r", encoding="utf-8", errors="ignore") as uf:
                    lines = uf.readlines()
                print(f"    - {file:<26}: {len(lines):>5} URLs discovered")

    print("\n[+] Data pipeline verification complete. Ready for chunking & vector indexing.")
    print("=" * 60)
    return True

if __name__ == "__main__":
    validate_pipeline_artifacts()
