---
title: Reusable tests
description: Leverage reusable tests to simplify test maintenance and streamline the management of large tests and test suites. Reusable tests reduce redundancy, ensuring consistent and reliable test execution across your system.
locale: en-US
release: australia
product: Automated Test Framework \(ATF\)
classification: automated-test-framework-atf
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Automated Test Framework \(ATF\) test types and techniques, Automated Test Framework \(ATF\), Testing and debugging applications, Building applications]
---

# Reusable tests

Leverage reusable tests to simplify test maintenance and streamline the management of large tests and test suites. Reusable tests reduce redundancy, ensuring consistent and reliable test execution across your system.

**Note:** A reusable test can be invoked only from another test \(a regular test or a reusable test\). The reusable test can’t be added to test suites individually.

Use the following related lists to pass variables from one test to another. Select **New** to create either the reusable input or output.

-   Reusable Input Variables: Contains the reusable input variables that are passed in from the parent test. The variable is passed from the test calling the current reusable test.
-   Reusable Output Variables: Contains the reusable output variables that are passed in from the child test. The variable is intended to be passed back up to the parent test calling the current reusable test.

![Screenshot showing input/output variables](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/application-development/automated-test-framework-atf/../image/atf-reusable-test-i:o.png)

**Note:** The reusable input and output variables that you create for the test are shown under the Reusable Input Variables and Reusable Output Variables related lists. The input variables are passed in from the parent test that is calling the current reusable test and is used by the reusable test. The output variables are passed back to the parent test and are used only by its test steps.

Use the Reusable Test test step category to access the created reusable test records. See [Reusable Tests category](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/application-development/automated-test-framework-atf/../reference/test-steps-reusable-tests-category.md) for more information.

-   **[Create a reusable test](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/application-development/automated-test-framework-atf/../task/atf-create-reusable-tests.md)**  
Create a reusable test to avoid redundancy, ensuring better test maintenance and reliable test execution across the instance.

**Parent Topic:**[Automated Test Framework \(ATF\) test types and techniques](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/application-development/automated-test-framework-atf/atf-test-type-testing.md)

**Related topics**  


[Mutually exclusive tests](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/application-development/automated-test-framework-atf/mutual-exclusion-rule.md)

[Quick start tests](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/application-development/automated-test-framework-atf/quick-start-tests.md)

[Parallel testing](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/application-development/automated-test-framework-atf/parallel-testing.md)

[Accelerate ATF tests failure resolution](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/application-development/automated-test-framework-atf/../task/atf-test-triage.md)

[Performance profiling](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/application-development/automated-test-framework-atf/atf-perf-prof.md#)

