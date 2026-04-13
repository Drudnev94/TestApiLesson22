import pytest
from api.api_post_banner import PostBaner
from api.api_delete_banner import ApiDeleteBanner
from api.api_get_banner import APIGetBanner
from api.api_patch_baner import ApiPatchBaner

@pytest.fixture
def post_banner_api():
    return PostBaner()

@pytest.fixture
def delete_banner_api():
    return ApiDeleteBanner()

@pytest.fixture
def api_get_banner():
    return APIGetBanner()

@pytest.fixture
def api_patch_banner():
    return ApiPatchBaner()
