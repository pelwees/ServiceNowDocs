---
title: SC Shopping Cart widget
description: The SC Shopping Cart widget \(sc-shopping-cart-v2\), used with Service Catalog, stores all your orders at one place. You can use this base system widget as-is in your portal or clone it to suit your own business needs.
locale: en-US
release: australia
product: Service Portal
classification: service-portal
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 5
breadcrumb: [Service Catalog widgets, Widget library, Using portal widgets, Configuring Service Portal, Service Portal, Configure UIs and portals, Configure user experiences]
---

# SC Shopping Cart widget

The SC Shopping Cart widget \(sc-shopping-cart-v2\), used with Service Catalog, stores all your orders at one place. You can use this base system widget as-is in your portal or clone it to suit your own business needs.

Use the shopping cart widget to:

-   Control the quantity of items in the cart.
-   Add items to a cart. This information is stored in the sc\_cart table.
-   Define who the items are being requested for.
-   Save specific items together as a bundle, which can be reloaded later. You can replace the cart items with the saved bundles, or add the bundles to the cart items.
-   Remove all items from your cart.

![Screenshot for the SC Shopping Cart widget](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-user-interface/service-portal/../../../product/service-catalog-management/image/SCShoppingCart.png "SC Shopping Cart widget")

## Instance options

Use the widget instance options to customize the settings for the SC Shopping Cart widget. To customize the settings for this widget, press the Ctrl key, click on the widget, and select **Instance Options**.

|Field|Description|
|-----|-----------|
|Presentation|
|Bootstrap color|Color scheme for the widget. The default colors are defined by the portal theme, but if you want the instance to have a specific color, select the option from the list.|
|Behavior|
|Cart Template|Enter the name of a ng-template you want to use to provide a different template for the shopping cart. By default, two ng-templates are provided: `small_shopping_cart_v2.html` and `large_shopping_cart_v2.html`.|
|Auto update cart|Automatically updates the cart across all sessions.|

-   **[Enable the Shopping Cart widget](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-user-interface/service-portal/enable-shopping-cart.md)**  
The shopping cart widget is enabled automatically for instances upgrading to Istanbul, however, there are several ways to manually enable or disable the widget.
-   **[Enable automatic updates to the shopping cart](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-user-interface/service-portal/../task/enable-auto-update-cart.md)**  
Automatically update the shopping cart across all sessions when users make changes from multiple tabs and platforms.

**Parent Topic:**[Service Catalog widgets](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-user-interface/service-portal/sc-widgets.md)

**Related topics**  


[Catalog Content widget](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-user-interface/service-portal/catalog-content-widget.md)

[Catalog Homepage Search widget](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-user-interface/service-portal/cat-homepage-search-widget.md)

[Recent &amp; Popular Items widget](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-user-interface/service-portal/recent-and-popular-items-widget.md)

[Request Fields widget](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-user-interface/service-portal/request-fields-widget.md)

[Requested Items widget](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-user-interface/service-portal/requested-items-widget.md)

[Requests and Approvals widget](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-user-interface/service-portal/requests-and-approvals-widget.md)

[SC Catalog Item widget](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-user-interface/service-portal/sc-catalog-item-widget.md)

[SC Categories widget](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-user-interface/service-portal/sc-categories-widget.md)

[SC Category Page widget](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-user-interface/service-portal/sc-category-page-widget.md)

[SC Order Guide widget](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-user-interface/service-portal/sc-order-guide-widget.md)

[SC Popular Items widget](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-user-interface/service-portal/sc-popular-items.md)

[SC Save Bundles widget](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-user-interface/service-portal/save-bundles-widget.md)

[SC Saved Carts widget](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-user-interface/service-portal/saved-cart-widget.md)

[SC Scroll to top widget](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-user-interface/service-portal/sc-scroll-to-top.md)

[SP Variable Editor widget](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-user-interface/service-portal/variable-editor-widget.md)

[SC Wish List Cart widget](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-user-interface/service-portal/sc-wish-list.md)

[Create and edit a page using the Service Portal Designer](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-user-interface/service-portal/../task/t_ConfigureAPage.md#)

[Configure widget instances](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-user-interface/service-portal/c_ConfigureWidgetInstances.md)

[Clone a widget](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-user-interface/service-portal/../task/t_CloneAndEditAWidget.md)

[Add a catalog item to the shopping cart](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/servicenow-platform/service-catalog/add-to-cart-portal.md)

