# Databricks API Medallion Pipeline

## 🚀 Overview
This project demonstrates a production-grade real-time data pipeline using Databricks and Delta Lake.

## 🏗 Architecture
API → Bronze → Silver → Gold

## ⚙️ Tech Stack
- Azure Databricks
- PySpark
- Delta Lake
- ADLS Gen2
- REST API

## 🔥 Features
- API ingestion with retry logic
- Incremental data processing
- Structured Streaming pipeline
- Watermarking for late data
- Deduplication using primary key

## ▶️ Execution Steps

1. Run Bronze notebook (batch ingestion)
2. Start Silver streaming job
3. Start Gold streaming job

## 📊 Output
- Bronze: Raw API data
- Silver: Cleaned data
- Gold: Aggregated insights

## 🧠 Use Case
Real-time ingestion and processing of API data for analytics.
