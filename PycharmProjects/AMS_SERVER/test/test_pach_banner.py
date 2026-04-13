class TestApiPatchBanner:


    def test_api_patch_banner(srlf,api_patch_banner):
        """Аргументы: id,название(srt),приоритет,мах_кол_показов,время_отображения, платформы"""
        response = api_patch_banner.api_patch_banner(109,"РЕНЕЙМ",10,45,200,(11,12))
        response = response.json()
        print(response)