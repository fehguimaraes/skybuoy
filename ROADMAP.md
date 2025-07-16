# 🧭 SkyBuoy Roadmap

This roadmap outlines the planned improvements and goals for **SkyBuoy**, a personal learning project and portfolio piece that brings aviation weather data into the cloud (specifically Elasticsearch).

---

## ✅ Phase 1 – Working MVP (complete!)

- [x] Fetch METAR data from the AWC API
- [x] Index data into Elasticsearch
- [x] Use `.env` for secure configuration
- [x] Create ingest pipeline in Elasticsearch to parse date fields
- [x] Avoid duplicate documents using unique IDs
- [x] Basic Dockerfile added 🐳

---

## 🔵 Phase 2 – Code Structure

🎯 Goal: make the code modular, maintainable, and dev-friendly

- [ ] Split code into modules:
  - `fetch.py` (data ingestion)
  - `index.py` (Elasticsearch indexing)
  - `config.py` (env & constants)
- [ ] Add logging capabilities
- [ ] Consolidate dependencies in `requirements.txt` or migrate to `pyproject.toml`
- [ ] Document the Elasticsearch side in the README
- [ ] Add Elasticsearch setup code (auto-create index templates, ingest pipeline, etc.)

---

## 🟡 Phase 3 – Automation & Portability

🎯 Goal: run continuously and reliably in various environments

- [ ] Refactor Dockerfile
- [ ] Add `docker-compose.yml`
- [ ] Implement scheduled execution:
  - `cron` or `schedule`, preferably so it runs at every hour (as opposed to every 60 minutes as it is now)
- [ ] Support multiple stations (via list or config) with bulk indexing

---

## 🟣 Phase 4 – Visualization & Query Tools

🎯 Goal: make the data easily accessible and useful

- [ ] Build and package a Kibana dashboard to explore indexed METARs
- More to be added

---

## 🟤 Phase 5 – Robustness & Portfolio Polish

🎯 Goal: make it clean, testable, and showcase-ready

- [ ] Write simple tests with `pytest`
- [ ] Add GitHub Actions for automated checks
- [ ] Add badges (build, license, Python version, etc.) to the README
- [ ] Design a logo or project icon

---

## 🌈 Extra Ideas (fun or future features)

- [ ] Real-time alerts via Discord, Telegram, or email for severe conditions
- [ ] Create a simple REST API with Flask to expose the data
- More to be added
