# License To Kill

## Introduction

State-of-the art license management solutions protect software vendors and solutions from fraud, illegal distribution, and manipulation of proprietary code. Among industrial control system (ICS) vendors, Wibu-Systems AG’s CodeMeter product is fairly ubiquitous. CodeMeter is integrated into products from vendors who have a significant customer presence in industries such as pharmaceuticals, manufacturing, automotive developers, and many others. It provides a full-scale license management solution and antipiracy protection, in addition to other encryption services that—big picture—act as a security blanket guarding the intellectual property of companies worldwide. 

Claroty’s research team has examined this powerful utility because of its large market presence among ICS vendors and found six vulnerabilities that collectively were assessed the highest criticality (10.0) by the Cybersecurity and Infrastructure Security Agency (CISA). These vulnerabilities may be attacked remotely and without authentication, and provide attackers with the equivalent of administrator access to critical systems. Successful exploits could enable either remote code execution or cause a denial-of-service condition affecting the availability of an industrial device or service.

The vulnerabilities range from memory corruption vulnerabilities such as buffer overflows, to cryptographic flaws where the improper encryption strength was used, or cryptographic signatures were improperly validated. 

Wibu-Systems has made fixes available for all of the vulnerabilities privately disclosed by Claroty researchers in version 7.10 of CodeMeter. All versions of CodeMeter prior to 7.10 are affected by these vulnerabilities in some way. The larger issue, as is common in the ICS domain, is the unlikelihood of widespread implementation of the respective patches. CodeMeter is a widely deployed third-party tool that is integrated into numerous products; organizations may not be aware their product has CodeMeter embedded, for example, or may not have a readily available update mechanism. 

Hoping to improve awareness of whether organizations are vulnerable to these flaws, Claroty researchers have published a tool that allows organizations to test whether they’re running a vulnerable version of CodeMeter, and can use that information to make a determination how to move forward with regard to patching. The tool is available at https://info.claroty.com/wibu-codemeter.

What follows is an in-depth description of the approaches researchers took in, first, understanding the CodeMeter licensing scheme in order to eventually parse CodeMeter licenses, modify existing licenses, and even forge valid licenses. Then we’ll describe how researchers built a novel fuzzer to find vulnerabilities in the CodeMeter license-parsing mechanism that allowed researchers to generate corrupted licenses that could cause machines to crash by injecting malicious JavaScript from an attacker-controlled website. 
We’ll also describe a second attack vector that can, in cases, enable remote code execution on a device running CodeMeter. Researchers were able to crack the encryption protecting CodeMeter’s proprietary protocol in order to build their own CodeMeter API and client, and essentially have the ability to communicate with and send commands to any machine running CodeMeter. This allowed Claroty researchers to find additional memory corruption vulnerabilities and gain remote code execution without authentication. 

## How To Use

    python codemeter_port_check.py IP_ADDR


## Advisories
- [WIBU-SYSTEMS Advisories](https://www.wibu.com/support/security-advisories.html)
- [ICS-CERT Advisory](https://us-cert.cisa.gov/ics/advisories/icsa-20-203-01)
- [List of Affected Companies](https://www.claroty.com/2020/09/08/blog-research-vendors-affected-by-wibu-codemeter-vulnerabilities/)

## Claroty Links
- [Blog](http://claroty.com/2020/09/08/blog-research-wibu-codemeter-vulnerabilities/)
- [Technical Paper](https://info.claroty.com/license-to-kill-leveraging-license-management-to-attack-ics-networks?hs_preview=FjgYiWqR-34506376052)

## Claroty Tools
- [Claroty's Vulnerability Tester Webpage](https://info.claroty.com/wibu-codemeter)
- [CodeMeter Port Checker](https://github.com/ClarotyICS/License-to-Kill)