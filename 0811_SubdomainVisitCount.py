from typing import List
from collections import defaultdict


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        count_dict = defaultdict(int)

        for domain_info in cpdomains:
            count, domain = domain_info.split(' ')
            count = int(count)

            subdomains = domain.split('.')
            for i in range(len(subdomains)):
                subdomain = '.'.join(subdomains[i:])

                count_dict[subdomain] += count

        result = [f"{cnt} {dmn}" for dmn, cnt in count_dict.items()]
        return result
