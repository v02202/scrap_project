// pre-populate the data at the time of the creation of MongoDB
// pre-create users
db = db.getSiblingDB("mongodb");
db.scrapy_tb.drop();

db.scrapy_tb.insertMany([
    {
        "url": "test_url",
        "detail": "test_detail",
        "website_name": "test_name"
    },
    {
        "id": 2,
        "name": "Cow",
        "type": "domestic"
    }
]);