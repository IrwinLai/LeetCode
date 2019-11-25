class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        s = []
        for i in emails:
            tem = i.split('@')
            alice = tem[0].split('+')
            alice = [(''.join(alice[0].split('.')))]
            alice.append(tem[1])
            s.append('@'.join(alice))

        return len(set(s))
            