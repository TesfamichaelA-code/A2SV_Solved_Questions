class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        sub_domains = defaultdict(int)
        for domain in cpdomains:
            times, full_domain = domain.split(" ")
            count = int(times)
            urls = full_domain.split(".")
            for i in range(len(urls)):
                sub_domain = ".".join(urls[i:])
                sub_domains[sub_domain] += count
        result = []
        for domain, total in sub_domains.items():
            result.append(str(total)+ " " + domain)
        
        return result
            
       



        