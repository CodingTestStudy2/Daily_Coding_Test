'''
1. 아이디어 :
    . 을 기준으로 버전 나눠서 비교
2. 시간복잡도 :
    O(n)
3. 자료구조/알고리즘 :
'''

class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """

        # print('111'.find('.'))

        while True:
            if version1 == '' and version2 == '':
                return 0

            v1_idx = version1.find('.')
            v2_idx = version2.find('.')

            # print('version1, version2, v1_idx, v2_idx:', version1, version2, v1_idx, v2_idx)
            # print('version2, len(version2), v2_idx:', version2, len(version2), v2_idx)

            v1_part = ''
            v2_part = ''
            if v1_idx == -1 and len(version1) == 0:
                v1_part = '0'
                version1 = ''
            elif v1_idx == -1 and len(version1) != 0:
                v1_part = version1
                version1 = ''
            else:
                v1_part = version1[:v1_idx]
                version1 = version1[v1_idx+1:]

            if v2_idx == -1 and len(version2) == 0:
                v2_part = '0'
                version2 = ''
            elif v2_idx == -1 and len(version2) != 0:
                v2_part = version2
                version2 = ''
            else:
                v2_part = version2[:v2_idx]
                version2 = version2[v2_idx+1:]

            # print('v1_part, v2_part:', v1_part, v2_part)
            
            if int(v1_part) < int(v2_part):
                return -1
            elif int(v1_part) > int(v2_part):
                return 1


        