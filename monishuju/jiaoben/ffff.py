# _*_ coding:utf-8 _*_

from faker import Faker
fake = Faker()
name = fake.name()
address = fake.address()
print(name)
print(address)

