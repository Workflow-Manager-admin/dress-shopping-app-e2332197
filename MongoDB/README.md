# MongoDB Container – Dress Shopping App

This folder contains the supporting database definitions and scripts for the Dress Shopping App.

## Collections and Data Models

- `users`: Stores all user profiles
  - name, phone_number _(unique)_, chest_size, favorite_brand, timestamps
- `dresses`: Dress catalog and inventory
  - name, image_url, price, brand, size, quantity, description, timestamps
- `orders`: Stores all placed orders
  - user_id, dress_id, quantity, total_amount, payment_status, etc.

See [`models.py`](models.py) for schemas.

## Database Initialization

Run `init_db.py` to set up collections and indexes after connecting MongoDB.

```bash
export MONGODB_URI="mongodb://username:password@host:port/db"
python MongoDB/init_db.py
```

## Integration Guidance

- The `MONGODB_URI` environment variable must be set with the full MongoDB connection string (for dev/CI/CD).
- Backend app should use the same database and collection names as referenced here.
- Use PyMongo for direct access or ODMs like Beanie/MongoEngine as required by application code.

## Notes

- This folder is NOT a standalone container. It's meant to support the monolithic container integration, enforcing data integrity and performance via proper indexing.
- Update schemas and scripts if business model changes.
