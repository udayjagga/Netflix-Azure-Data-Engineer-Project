# Netflix-Azure-Data-Engineer-Project

Developed end-to-end ETL pipeline that transforms Netflix data from raw formats into high-quality, structured data, ready for advanced analytics—leveraging the Medallion Architecture and Delta Lake. 💡

🔷𝐁𝐫𝐨𝐧𝐳𝐞 𝐋𝐚𝐲𝐞𝐫 – 𝐑𝐚𝐰 𝐃𝐚𝐭𝐚 𝐈𝐧𝐠𝐞𝐬𝐭𝐢𝐨𝐧:
Used Azure Data Factory to ingest data from multiple sources (CSV, REST API, GitHub) into Azure Data Lake Storage Gen2 (𝐀𝐃𝐋𝐒 𝐆𝐞𝐧𝟐).
Designed a parameterized pipeline to handle multiple files, optimizing ingestion based on file size and activity.

🔶𝐒𝐢𝐥𝐯𝐞𝐫 𝐋𝐚𝐲𝐞𝐫 – 𝐃𝐚𝐭𝐚 𝐓𝐫𝐚𝐧𝐬𝐟𝐨𝐫𝐦𝐚𝐭𝐢𝐨𝐧:
Utilized Azure Databricks and PySpark for data cleansing and transformation.
Connected ADB to ADLS via Azure Access Connector and implemented Unity Catalog for metadata management and data governance.
Stored the cleaned data back into the Silver Layer in Parquet format, ready for aggregation.

🟡𝐆𝐨𝐥𝐝 𝐋𝐚𝐲𝐞𝐫 – 𝐑𝐞𝐚𝐝𝐲 𝐟𝐨𝐫 𝐀𝐧𝐚𝐥𝐲𝐭𝐢𝐜𝐬:
Aggregated and optimized data stored in Delta Lake format, ensuring transactional consistency and enabling time travel for historical analysis.
Created Delta Tables and used SQL in Databricks for efficient querying.
Enabled schema evolution to handle changes in incoming data seamlessly, making the dataset analytics-ready.

💡𝐓𝐞𝐜𝐡𝐧𝐨𝐥𝐨𝐠𝐢𝐞𝐬 𝐔𝐬𝐞𝐝:
✅ Azure Data Lake Storage Gen2 (ADLS Gen2)
✅ Azure Data Factory (Dynamic Pipeline)
✅ Azure Databricks
✅ Azure Access Connector
✅ PySpark
✅ Microsoft Entra ID
