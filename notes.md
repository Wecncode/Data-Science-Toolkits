# Data Intuition & Spreadsheets <br>
# Wecncode DS101 Lecture Notes

## Data Intuition & Spreadsheets
*Goal: Understand the shape of data before writing code.*

* **Data Types (The Primitives):**
    * **Numerical:** Quantitative data. Can be **Continuous** (e.g., height, temperature; infinite precision) or **Discrete** (e.g., number of clicks; integer values).
    * **Categorical:** Qualitative data. Can be **Ordinal** (has an inherent order, e.g., "Small", "Medium", "Large") or **Nominal** (no order, e.g., "Red", "Blue").
* **Central Tendency (Finding the Center):**
    * **Mean:** The average. Highly sensitive to outliers.
    * **Median:** The middle value when sorted. Robust to outliers (If Bill Gates walks into a bar, the *mean* wealth skyrockets, but the *median* stays roughly the same).
    * **Mode:** The most frequent value. Best for categorical data.
* **Standard Deviation (σ):** A measure of how spread out the data is around the mean (μ). A low σ means the data is tightly clustered; a high σ means it's spread out. 
    `σ = sqrt( Σ(xi - μ)² / N )`
* **Correlation vs. Causation:** Correlation measures how two variables move together (from -1 to 1). Causation implies one event dictates the other. *Always plot your data to spot spurious correlations* (e.g., ice cream sales and shark attacks are highly correlated, but the hidden variable is summer weather).

---

## Arrays & Memory (NumPy)
*Goal: Understand why Python lists are too slow for Big Data.*

* **Contiguous Memory:** Standard Python lists are arrays of *pointers* to objects scattered across RAM. This destroys CPU cache efficiency. NumPy arrays allocate a single, contiguous block of memory containing raw C-types (like `int32` or `float64`).
* **Time Complexity:** Lookups in arrays are O(1) because the memory address is mathematically predictable: `address = start_address + (index * element_size)`.
* **Vectorization (SIMD):** Single Instruction, Multiple Data. Instead of using a Python `for` loop (which involves interpreter overhead and type-checking on every iteration), vectorization pushes the loop down to optimized C or Fortran code, operating on entire blocks of data simultaneously at the hardware level.
* **Broadcasting:** NumPy's rule for operating on arrays of different shapes. If you add a 1x3 array to a 3x3 array, NumPy "broadcasts" the smaller array across the larger one virtually, saving memory by not creating physical copies.

---

## Data Manipulation (Pandas)
*Goal: Master the grammar of data transformation.*

* **Series vs. DataFrames:** A `Series` is a 1D labeled array (like a column in a database). A `DataFrame` is a 2D table composed of multiple Series that share the same index.
* **Indexing Paradigms:**
    * `df.loc[]`: Label-based indexing (e.g., "Get the row with the string index 'User_42'").
    * `df.iloc[]`: Integer-position based indexing (e.g., "Get the 5th row in memory").
* **Boolean Masking:** Filtering without loops. Creating an array of True/False values and applying it to the DataFrame. 
    `df[df['age'] > 30]` creates a mask and returns only the rows where the condition is `True`.
* **Handling Missing Values (NaN):** NaN (Not a Number) is a float. You can either **Drop** them (if you have plenty of data) or **Impute** them (fill them with the mean, median, or a predicted value to save the row).
* **Split-Apply-Combine:** The logic behind `.groupby()`. You split data by a category, apply an aggregation function (like `sum()` or `mean()`), and combine the results into a new summary table.

---

## Visualization & Storytelling
*Goal: Prove your point using pixels.*

* **The Grammar of Graphics:** Every chart consists of three elements:
    1.  **Data:** The actual variables.
    2.  **Geometries (Geoms):** The shapes used to represent data (bars, points, lines).
    3.  **Aesthetics (Aes):** How data maps to visual properties (x/y coordinates, color, size).
* **Anscombe's Quartet:** Four distinct datasets that have identical summary statistics (same mean, variance, and correlation). However, when plotted, they look entirely different. **Lesson:** Always visualize your data; statistics can lie.
* **Matplotlib Object-Oriented API:** Don't use `plt.plot()` (state-machine method). Use `fig, ax = plt.subplots()`. The `Figure` is the blank canvas; the `Axes` is the actual chart. This allows you to build complex dashboards with multiple subplots.

---

## Databases & SQL
*Goal: Extracting data from relational systems.*

* **Relational Models:** Storing data in tables to avoid redundancy (Normalization). Instead of writing "New York" a million times, you write it once in a Cities table and reference it via an ID.
* **Keys:**
    * **Primary Key:** A unique identifier for a row in a table (e.g., `user_id`).
    * **Foreign Key:** A column that links to the Primary Key of another table.
* **JOINs:** Combining tables based on related keys.
    * **INNER JOIN:** Returns only records with matching values in both tables (Intersection).
    * **LEFT JOIN:** Returns all records from the left table, and the matched records from the right table.
* **Indexing (B-Trees):** Creating an index is like creating an alphabetical table of contents at the back of a book. It changes a full table scan O(N) into a tree traversal O(log N). *Tradeoff:* Indexes consume storage and slow down `INSERT`/`UPDATE` operations.

---

## Machine Learning I (Under the Hood)
*Goal: Build predictive engines from scratch.*

* **Supervised Learning:** Providing an algorithm with features (X) and known labels (Y) so it can learn the mapping function f(X) = Y.
* **Loss Functions:** Mathematical ways to measure how "wrong" a model is. For Linear Regression, we use Mean Squared Error (MSE):
    `J(θ) = (1/2m) * Σ (hθ(x(i)) - y(i))²`
* **Gradient Descent:** An optimization algorithm. To minimize the Loss Function, you calculate the derivative (the slope) of the loss curve with respect to your weights (θ), and take a small step (Learning Rate, α) in the opposite direction.
    `θj = θj - α * (∂/∂θj) J(θ)`
* **K-Nearest Neighbors (KNN):** A "lazy" algorithm. It doesn't calculate weights; it simply stores the training data. When given a new point, it calculates the geometric distance (Euclidean or Manhattan) to all stored points and takes a majority vote of the K closest neighbors.

---

## Machine Learning II (The Abstraction)
*Goal: Using `scikit-learn` safely without overfitting.*

* **Train/Test Splits:** Never test your model on the data you used to train it. That is memorization, not learning. Always split data (e.g., 80% train, 20% test).
* **Cross-Validation:** To ensure your split wasn't a "lucky draw," K-Fold CV splits the data into K chunks, trains the model K times (using a different chunk as the test set each time), and averages the scores.
* **Evaluation Metrics (Classification):** Accuracy is dangerous with imbalanced data (e.g., if a disease occurs in 1% of people, a model that always guesses "No" is 99% accurate but useless).
    * **Precision:** Out of all instances the model predicted positive, how many were actually positive? (Minimizes False Positives).
    * **Recall:** Out of all actual positive instances, how many did the model find? (Minimizes False Negatives).
* **Ensemble Methods (Random Forests):** A single Decision Tree is prone to overfitting. A Random Forest trains hundreds of different trees on random subsets of the data and random subsets of features (Bagging). The final prediction is the average (regression) or majority vote (classification) of all trees, creating a highly robust model.
