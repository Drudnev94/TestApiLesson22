from test.json_for_post.base_api_docs import BaseApiDocs

class PayloadGenerator(BaseApiDocs):
        def test_get_docs(self):
            obj = {  "email": self.EMAIL, "password": self.PASSWORD,  "username": self.USERNAME }
            return obj

result = TestJsonForPost()
OBJ_FOR_POST = result.test_get_docs()
print(OBJ_FOR_POST)

# class TestJsonForPost(BaseApiDocs):
#     OBJ_FOR_POST = {
#   "email": "d@gmail.com",
#   "password": "123",
#   "username": "d123"
}
