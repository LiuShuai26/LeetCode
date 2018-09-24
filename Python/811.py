# 基础技巧题


class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        d = {}
        for item in cpdomains:
            web = item.split(' ')
            site = web[1]
            number = int(web[0])
            if site in d:
                d[site] += number
            else:
                d[site] = number
            site = site.split('.')
            if len(site) == 3:
                name = '.'.join(site[1:3])
                if name in d:
                    d[name] += number
                else:
                    d[name] = number
                name = '.'.join(site[2:3])
                if name in d:
                    d[name] += number
                else:
                    d[name] = number
            elif len(site) == 2:
                name = '.'.join(site[1:2])
                if name in d:
                    d[name] += number
                else:
                    d[name] = number
        return ["%d %s" % (d[k], k) for k in d]


cp = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com"]
s = Solution()

print(s.subdomainVisits(cpdomains=cp))
