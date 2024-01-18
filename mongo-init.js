// pre-populate the data at the time of the creation of MongoDB
// pre-create users
db.createUser(
    {
        user: 'user1',
        pwd: '123456',
        roles: [{
                role: 'readWrite',
                db: 'mongodb'
            }
        ]
    }
);