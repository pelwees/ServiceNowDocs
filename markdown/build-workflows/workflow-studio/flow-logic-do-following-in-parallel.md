---
title: Do the following in parallel flow logic
description: Run actions and subflows in separate paths within an isolated flow logic block.
locale: en-US
release: australia
product: Workflow Studio
classification: workflow-studio
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 5
breadcrumb: [Flow logic, Flows, subflows, and actions reference, Flows, subflows, and actions, Workflow Studio, Build workflows]
---

# Do the following in parallel flow logic

Run actions and subflows in separate paths within an isolated flow logic block.

With this flow logic, you can run actions and subflows in separate paths. If any action within the Do the following in parallel flow logic block must wait, other actions run until all paths within the block finish processing.

![Multiple paths in a Do the following in parallel flow logic block](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/build-workflows/workflow-studio/../images/flow-logic-do-in-parallel.png "Paths in a Do the following in parallel flow logic block")

**Note:** Paths in a Do the following in parallel flow logic block do not run in multiple threads, since a flow execution context runs in a single thread. However, there may be times when you want to run flows within separate contexts even though this may consume more of your instance's resources. To run subflows in separate flow contexts within the same flow, see [Dynamic flows](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/build-workflows/workflow-studio/flow-logic-dynamic-flow.md).

## Inputs

Do the following in parallel flow logic does not have field inputs. Instead, it displays a plus \(![New Branch Icon](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/build-workflows/workflow-studio/../../../build/app-engine-studio/image/plus-icon.png)\) icon that enables you to create a path with actions or subflows.

The actions and subflows in each path run until all tasks within the flow logic block have completed.

## Outputs

This flow logic has no outputs, but actions and subflows in each path may have outputs. While the flow is running, outputs from a path are only accessible to other actions in the same path. After the Do the following in parallel flow logic completes, its final outputs are accessible to the rest of the flow.

## Create two tasks in parallel when a change request is created

In this example, a flow triggers when a new change request is created. Using **Do the following in Parallel**, two tasks are created in separate paths and are assigned to different groups. The flow uses the **Number** field data pill from the triggering change request to display the number in the short description for the task record.

![Do the following in parallel example](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/build-workflows/workflow-studio/../images/parallel-example-1.png "Do the following in parallel flow logic inputs")

## Execution details

![Example execution details for a do the following in parallel flow](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/build-workflows/workflow-studio/../images/ex-details-do-following-parallel.png "Do the following in parallel execution details")

1.  The header shows the state, start time, and runtime for the flow logic.
2.  The Configuration Details section shows the state, start time, and runtime for each path in the flow logic block.

## General guidelines

-   **Avoid creating data dependencies between paths**

    Since a flow can run paths in any order, avoid creating data dependencies between separate paths. For example, do not have one path that creates a record and another path that updates the same record. The update record path may run before the create record path.

-   **Do not share data between paths**

    Workflow Studio prevents you from dragging data pills between paths because the system cannot determine which path will finish first to supply the output value.


**Parent Topic:**[Workflow Studio flow logic](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/build-workflows/workflow-studio/flow-logic.md)

**Related topics**  


[Append to Flow Variables flow logic](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/build-workflows/workflow-studio/../reference/append-to-flow-variables-flow-logic.md)

[Assign subflow outputs flow logic](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/build-workflows/workflow-studio/flow-logic-assign-subflow-outputs.md)

[Call a workflow flow logic](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/build-workflows/workflow-studio/flow-logic-call-workflow.md)

[Do the following until flow logic](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/build-workflows/workflow-studio/flow-logic-do-until.md)

[Dynamic flows flow logic](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/build-workflows/workflow-studio/flow-logic-dynamic-flow.md)

[End Flow flow logic](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/build-workflows/workflow-studio/flow-logic-end-action.md)

[Exit Loop flow logic](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/build-workflows/workflow-studio/../reference/exit-loop-flow-logic.md)

[For Each flow logic](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/build-workflows/workflow-studio/flow-logic-for-each.md)

[Get Flow Outputs flow logic](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/build-workflows/workflow-studio/../reference/get-flow-outputs-flow-logic.md)

[Go back to flow logic](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/build-workflows/workflow-studio/../reference/go-back-to-flow-logic.md)

[If flow logic](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/build-workflows/workflow-studio/flow-logic-if.md)

[Make a decision flow logic](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/build-workflows/workflow-studio/flow-logic-make-decision.md)

[Set Flow Variables flow logic](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/build-workflows/workflow-studio/flow-logic-set-flow-variables.md)

[Skip Iteration flow logic](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/build-workflows/workflow-studio/../reference/skip-iteration-flow-logic.md)

[Try flow logic](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/build-workflows/workflow-studio/flow-logic-try.md)

[Wait for a duration flow logic](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/build-workflows/workflow-studio/flow-logic-wait-for-a-duration.md)

