# Software Testing & Quality Assurance Workshops

This repository contains a collection of software testing workshops implemented in **Python**. The exercises cover core testing techniques including unit testing, mocking, web UI automation, fault localization, parameterized testing, mutation testing, and behavior-driven development (BDD).

The repository is organized as a series of workshops, each focusing on a different aspect of software testing and quality assurance.

---

## Module Map

The repository is organized into workshops that cover different software testing techniques and quality assurance practices:

### 📂 1_unit_testing_and_mocking (`/workshop_1`)

* **Core Concepts:** Unit Testing, Mocking, Stubbing, and Dependency Injection.
* **Implementation:** Uses `pytest` and `unittest` to test basic program behavior through `calculator.py` and `test_demo.py`. The workshop also demonstrates the use of `unittest.mock` to isolate external dependencies in `cart.py` and `product_db.py`.

### 📂 2_web_ui_automation (`/workshop_2`)

* **Core Concepts:** Browser Automation, End-to-End (E2E) Testing, and UI Interaction.
* **Implementation:** Uses Selenium WebDriver (`test_selenium.py`) to automate browser interactions, validate page behavior, and perform end-to-end testing scenarios.

### 📂 3_fault_localization_tarantula (`/workshop_3`)

* **Core Concepts:** Spectrum-Based Fault Localization (SBFL), Program Diagnostics, and Dynamic Analysis.
* **Implementation:** Implements the Tarantula fault localization algorithm (`tarantula-skeleton.py`) using test coverage information from `coverage.xml` to identify suspicious lines of code in programs such as `binarysearch.py` and `mid.py`.

### 📂 4_parameterized_and_boundary_testing (`/workshop_4`)

* **Core Concepts:** Boundary Value Analysis (BVA), Equivalence Partitioning, and Data-Driven Testing.
* **Implementation:** Uses `pytest` parameterization (`test_workshop_4.py`) to test functions with multiple input combinations, including boundary and edge cases.

### 📂 5_mutation_testing (`/workshop_5`)

* **Core Concepts:** Mutation Testing, Test Suite Evaluation, and Fault Injection.
* **Implementation:** Implements a custom mutator (`mutator-starter.py`) that introduces controlled changes into `sample_program.py`. The workshop evaluates how effectively the test suite detects injected faults through mutation testing.

### 📂 6_behavior_driven_development (`/workshop_6`)

* **Core Concepts:** Behavior-Driven Development (BDD), Gherkin Syntax, and Test Automation.
* **Implementation:** Uses Behave (`steps.py`) and Gherkin feature files (`yourturn.feature`) to describe application behavior and connect it to executable test definitions.

---


