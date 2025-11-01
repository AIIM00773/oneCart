

Front End :

1) General Landing page -- #done
2) Home Page  -- #done
3) Product Listings Page --#done
4) Cart page ---#done
5) Checkout Page ---#done 
6) Ai interface Page ---#done  
7) Profile Page 
8) Stores Page 
9) Login Page 
10) SignUp Page
11) About Page 
12) Support Page 




BACKEND 

User
 ├── id (PK)
 ├── username
 ├── email
 ├── password
 ├── phone_number
 ├── wallet_balance
 ├── first_name
 ├── last_name
 ├── date_joined
 └── last_login


Marketplace
 ├── id (PK)
 ├── name
 ├── api_base_url
 ├── api_key
 ├── description
 └── active
 |__logo  image 
 |__Rating
 |_decription 
 |_productRelationToken 


Product
 ├── id (PK)
 |
 |__Product Relation Token
 |
 ├── marketplace (FK → Marketplace)
 ├── external_id
 ├── title
 ├── description
 ├── price
 ├── currency
 ├── image_url
 ├── product_url
 ├── category
 ├── available
 └── created_at


CartItem
 ├── id (PK)
 |_Product RelationToken
 |
 ├── user (FK → User)
 ├── product (FK → Product)
 ├── quantity
 └── added_at


Order
 ├── id (PK)
 |_oder authenticationToken
 |
 |_order validation_token
 |
 |_orderRelationToken
 |
 ├── user (FK → User)
 ├── total_amount
 ├── status (choices: pending, processing, shipped, delivered, cancelled)
 ├── created_at
 └── updated_at


OrderItem
 ├── id (PK)
 ├── order (FK → Order)
 ├── product (FK → Product)
 ├── quantity
 └── price (price at the time of purchase)


AIPrompt (optional, for future AI feature)
 ├── id (PK)
 ├── user (FK → User)
 ├── prompt_text
 ├── response_json
 └── created_at













┌───────────┐         ┌───────────────┐
│ Marketplace │◄──────│    Product    │
│───────────│         │───────────────│
│ id (PK)   │         │ id (PK)       │
│ name      │         │ marketplace_id│FK
│ api_url   │         │ external_id   │
│ api_key   │         │ title         │
│ desc      │         │ description   │
│ active    │         │ price         │
└───────────┘         │ currency      │
                      │ image_url     │
                      │ product_url   │
                      │ category      │
                      │ available     │
                      │ created_at    │
                      └───────────────┘
                             ▲
                             │
                             │
                  ┌──────────┴───────────┐
                  │                      │
            ┌─────────────┐        ┌─────────────┐
            │  CartItem   │        │  OrderItem  │
            │─────────────│        │─────────────│
            │ id (PK)     │        │ id (PK)     │
            │ user_id(FK) │        │ order_id(FK)│
            │ product_id(FK)│      │ product_id(FK)│
            │ quantity    │        │ quantity    │
            │ added_at    │        │ price       │
            └─────────────┘        └─────────────┘
                  ▲                      ▲
                  │                      │
                  │                      │
                  │                      │
                ┌────────────────────────────┐
                │           Order            │
                │───────────────────────────│
                │ id (PK)                   │
                │ user_id(FK)               │
                │ total_amount              │
                │ status                    │
                │ created_at                │
                │ updated_at                │
                └───────────────────────────┘
                        ▲
                        │
                        │
                  ┌───────────┐
                  │   User    │
                  │───────────│
                  │ id (PK)   │
                  │ username  │
                  │ email     │
                  │ password  │
                  │ phone     │
                  │ wallet    │
                  │ date_joined│
                  │ last_login│
                  └───────────┘
                        ▲
                        │
              ┌─────────────────┐
              │    AIPrompt     │ (Optional)
              │─────────────────│
              │ id (PK)         │
              │ user_id (FK)    │
              │ prompt_text     │
              │ response_json   │
              │ created_at      │
              └─────────────────┘









[User Opens Site]
        │
        ▼
[Homepage]
- Search Bar
- Categories
- Featured Products
        │
        ▼
[User Enters Search Query]
        │
        ▼
[Backend Aggregator]
- Sends API requests to all integrated marketplaces
- Normalizes product data (title, price, image, rating, marketplace)
        │
        ▼
[Frontend Displays Results]
- Each product shows:
  - Name, image
  - Price
  - Rating
  - Marketplace logo/name
- User can compare prices & ratings
        │
        ▼
[User Adds Items to Cart]
- CartItem created per product:
  - user_id
  - product_id
  - marketplace_id
  - quantity
- Cart shows:
  - All items
  - Origin marketplace
  - Unified total price
        │
        ▼
[User Clicks Checkout]
        │
        ▼
[Backend Checkout Orchestrator]
- Fetch all CartItems
- Group items by marketplace_id internally
- Process single payment for total
- For each marketplace group:
    - Send order API request
    - Confirm success/failure
    - Store marketplace_order_id internally
- Create unified Order for user:
    - Links all OrderItems
    - Total sum
    - Status = pending/processing
        │
        ▼
[User Order Confirmation]
- Shows single Order ID
- Unified total
- Each item still shows marketplace origin
- Optionally: Expand for marketplace-specific order details
        │
        ▼
[Backend Order Tracking]
- Periodically query marketplaces for delivery status
- Update unified Order status
- Notify user of updates





                ┌─────────────────────┐
                │      User           │
                │────────────────────│
                │ Search Products     │
                │ Add to Cart         │
                │ Checkout            │
                └─────────┬──────────┘
                          │
                          ▼
                ┌─────────────────────┐
                │     Frontend        │
                │────────────────────│
                │ Displays Search     │
                │ Results (Price,    │
                │ Rating, Marketplace│
                │ Logo)               │
                │ Unified Cart &      │
                │ Checkout Button     │
                └─────────┬──────────┘
                          │
                          ▼
                ┌─────────────────────┐
                │     Backend         │
                │────────────────────│
                │ Aggregator: Fetch   │
                │ Products via APIs   │
                │ Normalize Data      │
                │ Cart Manager        │
                │ Order Manager       │
                │ Payment Processor   │
                │ Marketplace Adapter │
                └─────────┬──────────┘
                          │
          ┌───────────────┴───────────────┐
          ▼                               ▼
 ┌─────────────────────┐          ┌─────────────────────┐
 │  Marketplace APIs   │          │    Database         │
 │────────────────────│          │────────────────────│
 │ Amazon, Jumia, etc │          │ CartItem           │
 │ Place Orders       │          │ Order              │
 │ Track Orders       │          │ OrderItem          │
 │ Confirm Payments   │          │ Payment            │
 └────────────────────┘          │ User               │
                                 │ Product            │
                                 │ Marketplace        │
                                 └────────────────────┘
