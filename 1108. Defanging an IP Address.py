class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        l = address.split('.')
        defang = l[0]+'[.]'+l[1]+'[.]'+l[2]+'[.]'+l[3]
        return defang