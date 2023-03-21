"""This is the unittest for port_parser.py
This uses the sample log files provided by Jacob K. to test the parser functions
"""

from port_parser import parse_port

# key/val pairs are the sample log/list of strings for expected ports to be found
TEST_CASES = {
    """<86>May 28 08:21:45 okcjumperp01 sshd[7824]: Failed password for invalid user faketst from 10.1.1.150 port 11332 ssh2""": ["11332"],
    """<14>Aug 18 09:00:04 OKCDCP01.cat.com Microsoft-Windows-Security-Auditing[960]: A Kerberos service ticket was requested. Account Information: Account Name: FAKO@CAT.COM Account Domain: CAT.COM Logon GUID: {1234567A-890B-1234-C567-8D901EFG234H} Service Information: Service Name: krbtgt Service ID: S-1-2-34-5678901-2345678901-2345678901-987 Network Information: Client Address: ::ffff:172.16.0.2 Client Port: 19778 Additional Information: Ticket Options: 0x60810010 Ticket Encryption Type: 0x12 Failure Code: 0x0 Transited Services: - This event is generated every time access is requested to a resource such as a computer or a Windows service. The service name indicates the resource to which access was requested. This event can be correlated with Windows logon events by comparing the Logon GUID fields in each event. The logon event occurs on the machine that was accessed, which is often a different machine than the domain controller which issued the service ticket. Ticket options, encryption types, and failure codes are defined in RFC 4120.""": ["19778"],
    """<134>1 2020-08-14T18:28:15Z okc-1 FireWall 29610 - [action:"Accept"; conn_direction:"Outgoing"; flags:"1234567"; ifdir:"inbound"; ifname:"bond1.100"; logid:"0"; loguid:"{0x1234567,0x89,0xa012345b6,0x78c90123}"; origin:"172.16.0.1"; originsicname:"CN=okc-p,O=cat.com.8fp4ua"; sequencenum:"123"; time:"1597429695"; version:"4"; __policy_id_tag:"product=VPN-1 & FireWall-1[db_tag={ZYX9876-ABCD-0123-BETA-78C90123};mgmt=mgmt;date=1597388219;policy_name=Split-VPN-FW-Policy\]"; dst:"172.17.0.255 "; log_delay:"1597429695"; layer_name:"Split-VPN-FW-Policy Security"; layer_uuid:"1234567-1234-5678-ab90-78c9012345"; match_id:"25"; parent_rule:"0"; rule_action:"Accept"; rule_uid:" 1234567-1234-5678-ab90-78c9012345"; product:"VPN-1 & FireWall-1"; proto:"6"; s_port:"60641"; service:"80"; service_id:"http_"; src:"10.221.234.179";""": ["60641", "80"]
}

def test_parse_port():
    for string, expected_output in TEST_CASES.items():
        result = parse_port(string)
        assert expected_output == result