---
title: Configure Workplace entity and entity types
description: Create a business hierarchy based on your organization's businesses. Allocate workplace locations based on the business to which they’re associated with. Configure workplace entity types and workplace entities to create the structure. For example, add entity types such as Business Units, Marketing Units, and associate workplace entities such as ITSM, Facilities, and more under them.
locale: en-US
release: australia
product: Workplace Core
classification: workplace-core
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 6
breadcrumb: [Manage workplace safety activities, Workplace Core, Workplace Service Delivery, Employee Service Management]
---

# Configure Workplace entity and entity types

Create a business hierarchy based on your organization's businesses. Allocate workplace locations based on the business to which they’re associated with. Configure workplace entity types and workplace entities to create the structure. For example, add entity types such as Business Units, Marketing Units, and associate workplace entities such as ITSM, Facilities, and more under them.

The Workplace Core applications enable you to classify your workplace locations based on their cost center, department, and workplace entity. The workplace entity-based allocation helps you in create an organized business structure where you can configure parent-child-based hierarchies and manage various workplace-related activities. You can create a structure exactly as your organization's business by configuring workplace entity types and workplace entities. You can associate locations based on the business to which they’re associated with.

As a workplace manager, you can manage space allocations based on their entity levels that are set and verify proper space utilization according to business. You can visualize data on the stack plan and floor map based on the workplace entities that you’ve configured. You can view the space allocations of a building based on workplace entities. At any time, you can select a space and know its hierarchy level, that is, the details of its parent and child if present. This business-based hierarchy model, that is, workplace entity-based allocation, enables you to control the space consumption of each business in your organization. The Space Optimization dashboard also enables you to visualize data based on the different workplace entities configured. For more information about how workplace entities and other allocations work, refer to [Allocation - types, setting, and impact](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-core/../../workplace-space-management/reference/setting-an-allocation-and-its-impact.md).

**Important:** You can’t create a scenario based on workplace entities. You can only view and make map based space administration for workplace entities.

At any time, you can filter your workplace locations and perform various actions easily on these entities directly. The application enables you to specify an order to each entity type based on which a hierarchy is set. For a parent-child hierarchy, you can also perform direct actions on a parent if you want to implement the same throughout its child entities.

With the hierarchy-based configuration, you can perform the following actions:

-   You can create various entity types and set their level using the entity-mapping options. When you create workplace entities, you can assign them to these entity types.
-   You can set the order of an entity type based on its level in the hierarchy. The lower the order, the higher the entity type is set in the hierarchical structure. The lowest ordered entity type is set in the highest level in the hierarchy. For example, if you set ABC with order 1000 and XYZ with order 600 then XYZ is placed on top in the hierarchy level and ABC is set to lowest.
-   You can use the **Push down** option if you want to push down the workplace entity to child locations at any time. For more information about how an allocation works, refer to [Allocation - types, setting, and impact](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-core/../../workplace-space-management/reference/setting-an-allocation-and-its-impact.md).
-   You can activate or deactivate a workplace entity. Deactivating a workplace entity also deactivates the child workplace entity.

    **Important:** If the parent is inactive, you can’t activate a workplace entity.


-   **[Add a workplace entity type](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-core/../task/add-a-workplace-entity-type.md)**  
Create an entity type according to your organizational requirement. You can group your workplace entities under this entity type and perform various actions on all entities that belong to this type at a time.
-   **[Add workplace entities to an entity type](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-core/../task/add-workplace-entities-to-an-entity-type.md)**  
Create workplace entities based on your organization's business structure. Specify the entity type to which they belong. You can also specify a parent to the entity based on its hierarchy.

**Parent Topic:**[Manage workplace safety activities](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-core/manage-wsd-activites.md)

**Related topics**  


[Import your workspaces data from an Excel spreadsheet](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-core/../task/import-excel-spreadsheet-workspace-data-wsd.md)

[Add a space type configuration](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-core/../task/add-space-type-configuration-wsd.md)

[Configure a workplace card](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-core/../task/configure-workplace-card.md)

[Block a workplace location](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-core/../task/block-workplace-location.md)

[Managing Neighborhoods](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-core/../../workplace-space-management/concept/neighborhoods.md)

[Enable favorites option for Workplace Service Portal](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-core/../task/confgure-favourites-option-for-ws-portal-wsd.md)

[Create a workplace performer criteria](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-core/../task/create-workplace-performer-criteria.md)

[Mapping employees to their designated workspaces](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-core/mapping-employees-to-existing-work-locations-wsd.md)

[Assign the workplace user role to employees](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-core/../task/assign-workplace-user-role-to-employees-of-a-location-wsd.md)

[Configuring shifts for your workplace](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-core/configuring-shifts-for-your-workplace-wsd.md)

[Managing workplace shifts that you own](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-core/managing-shifts-you-own-wsd.md)

[Managing workplace reservations for employees](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-core/managing-workplace-reservations-wsd.md)

[Setting and tracking arrivals at the workplace](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-core/scheduling-employees-arrival-to-the-workplace-wsd.md)

[Approve employee workplace reservation requests](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-core/../task/approve-workplace-reservation-requests-wsd.md)

[Managing workplace tasks](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-core/managing-workplace-maintenance-tasks.md)

[Workplace knowledge management](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-core/workplace-knowledge-mgmt-wsd.md)

[QR code management](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-core/qr-code-mgmt.md)

[Location migration](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-core/location-migration.md)

[View workplace service usage analytics with Usage Insights](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-core/../reference/appsee-intergration-wsd.md)

