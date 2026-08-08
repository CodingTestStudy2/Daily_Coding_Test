class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # 정렬 기준으로 사용할 우선순위 저장
        order_dict = {char:i for i, char in enumerate(order)}

        # order에 없는 문자는 order 끝나고 맨 뒤에 붙임
        sorted_str = sorted(s, key=lambda x: order_dict.get(x, len(order)))

        return "".join(sorted_str)