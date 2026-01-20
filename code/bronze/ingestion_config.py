BASE_PATH = "/Volumes/workspace/bronze/source_systems/engineering"

INGESTION_CONFIG = [
    # CRM
    {
        "source": "crm",
        "path": f"{BASE_PATH}/source_crm/cust_info.csv",
        "table": "crm_cust_info"
    },
    {
        "source": "crm",
        "path": f"{BASE_PATH}/source_crm/prd_info.csv",
        "table": "crm_prd_info"
    },
    {
        "source": "crm",
        "path": f"{BASE_PATH}/source_crm/sales_details.csv",
        "table": "crm_sales_details"
    }
]
