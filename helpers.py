import faker


def fake_data_user():
    fake = faker.Faker()
    fake_name = fake.first_name()[0:5]
    fake_email = f'{fake.email()[0:5]}@gmail.com'
    fake_job = fake.job()
    return fake_name, fake_email, fake_job
