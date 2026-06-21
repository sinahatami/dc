<div align="center">
  <h1>🌐 Distributed Computing</h1>
  <p><b>Course Assignments & Final Project • University of Genoa</b></p>
</div>

Welcome to my repository for the **Distributed Computing (Large Scale Computing)** course. This repository contains a collection of assignments, discrete event simulations, PySpark data processing scripts, and the final course project.

Everything has been refactored, polished, and organized to ensure clean readability and execution.

---

## 📁 Repository Structure

The repository is logically divided into three main sections: **PySpark Assignments**, **Simulation Assignments**, and the **Final Project**.

### 1. 🧮 PySpark Assignments (`/pyspark_assignments`)

This directory contains Big Data analysis scripts designed to run on a Hadoop Distributed File System (HDFS) cluster using Apache Spark.

#### 🔹 Big Data Queries
* **`query_1_genre_overlap.py`**: Analyzes listening histories and user networks to extract the top overlapping music genres among connected friends.
* **`query_2_top_songs.py`**: Identifies the top 3 most listened-to songs among a specific user's network of friends.
* **`query_3_friend_recommendations.py`**: Advanced aggregation joining user networks, listening histories, and artist genres to recommend the top shared songs matching a user's preferred genres.

#### 🔹 Jupyter Notebooks
* **`LSC_assignment_1.ipynb` & `LSC_assignment_2.ipynb`**: Interactive notebooks containing exploratory data analysis, graph generation, and preliminary Large Scale Computing assignments.

---

### 2. ⚙️ Simulation Assignments (`/simulation_assignments`)

Custom simulation engines built in Python to model distributed systems, network queues, and epidemic spread.

* **`discrete_event_sim.py`**: The core simulation engine utilizing a priority queue (`heapq`) to manage events over time.
* **`sir.py`**: Simulates the spread of an infectious disease using the SIR (Susceptible-Infected-Recovered) epidemic model over a networked population.
* **`mmn_queue.py`**: An M/M/1 (and extensible M/M/n) queuing theory simulation evaluating average wait times against theoretical expectations.
* **`storage.py`**: A complex peer-to-peer storage simulation managing data blocks, redundancy ($k$-out-of-$n$ encoding), node downtimes, and network transfers.
* **`workloads.py`**: Parses and normalizes real-world high-performance computing traces (Mustang cluster) to feed into the simulations.
* **`configs/`**: Contains `.cfg` configuration files (`client_server.cfg`, `p2p.cfg`) defining the cluster properties for the storage simulations.

---

### 3. 🚀 Final Project (`/final_project`)

The culminating project of the course, focused on analyzing a large-scale network graph.

* **`superhero_network_analysis.ipynb`**: The main project notebook containing the methodology, PySpark execution, and visual analysis of the dataset.
* **`dataset/`**: Contains `vertices.csv` and `edges.csv` representing the network topology (e.g., nodes and connection edges for the "Superhero Fans" network).

---

## 🛠️ Setup & Execution

### Running the Python Simulations
The simulations rely on standard Python libraries. `storage.py` requires the `humanfriendly` library, and `sir.py` requires `matplotlib`.

```bash
# Set up a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install matplotlib humanfriendly

# Run the simulations
python simulation_assignments/sir.py
python simulation_assignments/mmn_queue.py
python simulation_assignments/storage.py simulation_assignments/configs/client_server.cfg
```

### Running PySpark Scripts
The PySpark scripts require a configured Spark environment and access to the specific CSV datasets hosted on HDFS (`hdfs:/user/user_lsc_78/...`). They should be submitted to the cluster via `spark-submit`:

```bash
spark-submit pyspark_assignments/query_1_genre_overlap.py
```

---

<div align="center">
  <i>Developed by Sina Hatami</i>
</div>
