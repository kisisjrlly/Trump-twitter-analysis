
#from MuNcut_v01 import MuNcut_main


#Best_cut_com_tweet,ss_tweet=MuNcut_main()


'''

一个分类的边界值
一个分类的tweet下标值

给原文档中每条tweet标上类别


'''
#Best_cut_com_tweet=[int(x) for x in list(Best_cut_com_tweet)]


b=[   0,  121,  253,  378,  512,  631,  756,  881, 1019, 1144, 1267,1399, 1527, 1655, 1781, 1909, 2033, 2159, 2277, 2420]
a=[127, 2, 3, 68, 1043, 2437, 7, 8, 157, 10, 11, 926, 778, 14, 15, 16, 17, 558, 2308, 20, 2081, 1403, 23, 24, 152, 26, 27, 2144, 197, 30, 31, 665, 1135, 34, 739, 36, 37, 1565, 39, 40, 41, 42, 43, 44, 45, 46, 47, 2180, 49, 2409, 1916, 2333, 53, 1280, 55, 56, 57, 58, 59, 2488, 61, 62, 63, 1542, 65, 66, 333, 207, 1382, 2218, 71, 1994, 1730, 1076, 75, 76, 77, 78, 1733, 80, 128, 431, 83, 84, 85, 86, 87, 298, 219, 90, 91, 92, 712, 94, 1301, 96, 97, 98, 2111, 100, 2372, 142, 103, 1715, 32, 106, 963, 108, 109, 110, 111, 112, 113, 114, 747, 116, 117, 118, 2513, 120, 121, 836, 493, 69, 1092, 81, 2084, 162, 129, 130, 131, 132, 133, 1108, 1612, 136, 412, 138, 105, 140, 468, 123, 216, 910, 2134, 146, 147, 148, 149, 150, 151, 1773, 153, 154, 155, 156, 245, 241, 159, 160, 1885, 361, 163, 568, 165, 166, 167, 1037, 169, 170, 1722, 815, 173, 174, 1700, 176, 1980, 178, 179, 180, 181, 182, 637, 184, 2502, 2410, 1813, 188, 550, 190, 262, 192, 1618, 1468, 195, 196, 4, 1184, 1758, 124, 201, 189, 203, 1498, 205, 206, 1559, 208, 209, 679, 1107, 212, 213, 214, 215, 1177, 217, 218, 29, 2295, 221, 222, 516, 1296, 970, 226, 227, 228, 229, 230, 231, 122, 233, 234, 235, 236, 237, 1593, 1094, 240, 19, 242, 243, 244, 102, 246, 1112, 248, 249, 285, 280, 269, 1471, 293, 275, 256, 1139, 2172, 1166, 260, 261, 423, 252, 264, 265, 1206, 548, 709, 355, 270, 271, 272, 273, 274, 319, 276, 592, 278, 1355, 376, 304, 282, 283, 284, 893, 64, 313, 288, 289, 290, 291, 292, 372, 294, 295, 1817, 297, 822, 299, 1998, 301, 302, 428, 287, 888, 306, 2533, 158, 309, 310, 311, 807, 253, 314, 250, 316, 750, 318, 183, 320, 321, 322, 810, 324, 325, 375, 599, 328, 1432, 330, 872, 332, 67, 334, 335, 336, 263, 338, 339, 935, 341, 490, 1459, 1127, 1701, 346, 2187, 848, 349, 1890, 351, 352, 353, 354, 2141, 356, 357, 358, 359, 1123, 281, 362, 363, 364, 365, 540, 367, 368, 369, 370, 2154, 254, 373, 374, 936, 473, 449, 2136, 470, 504, 576, 382, 383, 384, 1646, 386, 1589, 388, 389, 1001, 391, 392, 1544, 394, 1931, 436, 1940, 398, 399, 400, 401, 402, 403, 378, 405, 649, 1779, 408, 1735, 410, 411, 137, 413, 2298, 415, 416, 417, 418, 419, 1392, 421, 422, 461, 2223, 2382, 426, 404, 1171, 429, 1968, 2248, 432, 1283, 434, 435, 377, 437, 438, 439, 440, 441, 1848, 443, 444, 445, 446, 965, 448, 379, 756, 451, 2517, 453, 454, 455, 396, 962, 1190, 459, 460, 1547, 462, 2527, 2318, 465, 2181, 467, 141, 469, 255, 471, 1316, 427, 474, 1201, 476, 477, 1173, 479, 480, 1285, 482, 483, 484, 485, 486, 487, 1346, 489, 342, 491, 492, 125, 494, 495, 496, 497, 1087, 499, 500, 501, 502, 225, 380, 505, 2215, 1068, 752, 553, 630, 51, 614, 507, 514, 515, 1927, 517, 512, 519, 508, 1697, 522, 523, 2019, 525, 526, 527, 528, 1, 524, 1552, 532, 247, 575, 535, 536, 537, 538, 547, 366, 566, 542, 543, 534, 1424, 546, 511, 2374, 593, 200, 2353, 552, 390, 554, 708, 556, 623, 18, 559, 560, 561, 1175, 563, 564, 565, 1976, 567, 1815, 569, 2037, 1755, 2487, 1117, 574, 2145, 603, 1914, 578, 579, 580, 581, 1857, 583, 584, 539, 1163, 587, 1271, 2096, 1660, 544, 1443, 549, 6, 595, 596, 1996, 598, 327, 2449, 513, 602, 781, 1785, 605, 606, 395, 608, 988, 925, 611, 612, 613, 518, 1678, 616, 617, 1091, 619, 620, 2148, 622, 585, 624, 625, 626, 627, 640, 1499, 541, 877, 661, 655, 1460, 2446, 745, 632, 638, 639, 628, 641, 1278, 1069, 644, 1663, 646, 457, 1338, 406, 650, 651, 652, 653, 700, 729, 656, 2339, 488, 659, 2192, 1580, 662, 2206, 2152, 1841, 1917, 636, 668, 669, 670, 2412, 672, 673, 1491, 704, 666, 751, 866, 821, 680, 681, 682, 683, 1594, 685, 686, 687, 2460, 689, 690, 691, 692, 726, 694, 695, 696, 74, 698, 2496, 748, 701, 2461, 703, 635, 705, 1407, 707, 555, 268, 1683, 1833, 93, 633, 714, 715, 716, 1583, 1780, 719, 2514, 1458, 722, 723, 724, 1790, 1214, 727, 728, 667, 2063, 1494, 2396, 1473, 734, 735, 829, 1345, 738, 35, 740, 741, 220, 631, 744, 713, 746, 115, 660, 749, 317, 743, 591, 1891, 754, 677, 838, 1312, 787, 25, 634, 2445, 762, 1627, 1174, 765, 863, 450, 814, 767, 1074, 2003, 772, 773, 774, 775, 760, 777, 13, 1592, 780, 769, 782, 783, 784, 785, 312, 1369, 788, 1313, 790, 791, 1961, 793, 975, 921, 796, 1343, 798, 799, 800, 2330, 1698, 828, 804, 1472, 1002, 803, 808, 809, 323, 811, 812, 1144, 758, 172, 816, 817, 789, 819, 1601, 210, 88, 823, 792, 825, 826, 827, 759, 757, 794, 831, 832, 833, 2022, 835, 818, 837, 786, 839, 840, 841, 1965, 843, 844, 1816, 846, 847, 864, 849, 850, 2106, 852, 853, 854, 1761, 918, 857, 858, 859, 860, 1819, 557, 761, 776, 865, 678, 315, 868, 869, 870, 2027, 331, 2164, 874, 875, 876, 824, 2388, 879, 932, 2259, 895, 985, 999, 934, 1013, 887, 305, 779, 890, 891, 892, 2109, 894, 1058, 896, 2237, 898, 899, 900, 2379, 902, 995, 904, 905, 2345, 2252, 1957, 2336, 1507, 911, 886, 913, 914, 915, 916, 1267, 856, 919, 920, 795, 2008, 923, 1446, 1080, 889, 927, 928, 929, 930, 931, 883, 933, 903, 884, 326, 937, 2077, 939, 940, 941, 942, 909, 944, 945, 946, 947, 948, 1904, 950, 1745, 952, 953, 2408, 955, 956, 957, 943, 959, 960, 961, 2240, 107, 964, 447, 966, 1842, 968, 1119, 503, 971, 1687, 973, 974, 830, 2213, 977, 1989, 979, 980, 981, 982, 983, 1795, 958, 986, 987, 881, 989, 882, 991, 992, 993, 994, 1265, 996, 997, 998, 340, 1000, 1533, 1607, 1003, 1004, 1005, 1006, 1007, 2159, 880, 1010, 1011, 1012, 912, 1057, 9, 1099, 657, 1128, 1019, 1020, 1021, 1686, 1023, 1024, 1025, 1026, 1027, 1028, 1029, 1018, 1031, 1032, 1016, 1396, 1035, 1036, 168, 1038, 1039, 52, 1041, 2296, 5, 1044, 1045, 1806, 1047, 1048, 1138, 1919, 1051, 1052, 1053, 1054, 2397, 1056, 1046, 1086, 1059, 1060, 1061, 1082, 1063, 1064, 1078, 1838, 1067, 1238, 643, 1799, 2204, 1072, 1073, 770, 1075, 2203, 1143, 1033, 1079, 610, 1081, 2370, 1335, 1084, 1085, 1435, 498, 1088, 1479, 1090, 618, 2001, 1093, 1237, 1095, 1231, 1097, 1098, 1137, 1972, 1101, 1102, 1049, 2358, 1105, 1260, 211, 134, 1109, 2000, 1111, 1249, 1106, 1114, 175, 1116, 573, 1118, 969, 1120, 1121, 1122, 360, 2054, 1125, 1126, 344, 251, 1129, 1261, 1977, 1132, 2424, 1274, 1545, 1136, 1030, 1304, 257, 2190, 1141, 1142, 266, 1215, 1167, 1248, 1169, 2499, 1149, 1150, 1151, 1152, 1548, 1154, 1155, 1156, 1157, 1158, 2286, 409, 1161, 1162, 1241, 1242, 1165, 259, 586, 1168, 1148, 1170, 1113, 1172, 1598, 1555, 562, 1264, 126, 1178, 1179, 1180, 1181, 1182, 1183, 990, 1185, 1186, 2175, 1188, 1189, 2362, 1191, 1192, 1015, 1194, 1195, 1196, 1197, 1198, 2506, 1226, 1176, 1202, 1203, 1204, 1205, 1243, 1207, 1200, 1209, 1210, 1211, 1212, 1213, 736, 1153, 2032, 1217, 1218, 1219, 2355, 1221, 1193, 1223, 1224, 1225, 1240, 1227, 1228, 1229, 1230, 1282, 1077, 938, 1535, 1235, 742, 1252, 2360, 1239, 1236, 475, 239, 1232, 1244, 1245, 1246, 1247, 1222, 54, 1250, 1251, 1164, 1253, 2371, 1255, 1256, 1257, 1258, 1259, 972, 1718, 1262, 1263, 1353, 224, 1374, 1307, 1305, 1289, 533, 1311, 1272, 1453, 2332, 1275, 1276, 1277, 642, 688, 1969, 1281, 1433, 577, 1284, 481, 1286, 1327, 1288, 1543, 1290, 1291, 1292, 1293, 2009, 1295, 885, 1297, 1298, 1299, 1300, 95, 1677, 2191, 1017, 1509, 1303, 917, 1308, 1309, 1310, 588, 755, 813, 2067, 1315, 472, 1317, 1633, 1319, 570, 1321, 1322, 725, 1324, 1325, 1326, 1368, 1328, 1329, 1330, 1331, 1332, 1401, 1334, 1470, 1336, 1337, 648, 1339, 1340, 1341, 2500, 797, 1344, 737, 658, 1347, 1348, 1624, 1350, 1351, 1352, 1145, 1354, 279, 1066, 1357, 1358, 1359, 414, 1361, 1362, 1363, 1364, 1365, 1366, 1420, 1266, 2055, 1370, 1371, 1372, 1373, 1287, 1375, 1376, 1377, 1378, 2512, 2161, 1381, 1306, 1383, 2010, 1656, 1386, 1387, 1388, 674, 1390, 1391, 145, 1393, 1410, 1495, 1991, 1418, 1523, 1652, 1839, 1268, 1402, 2274, 1404, 1405, 1406, 706, 1408, 1409, 1394, 1411, 2305, 1413, 1414, 1415, 1416, 1417, 1918, 1419, 1367, 1897, 1422, 1423, 545, 1664, 1398, 1427, 1428, 1429, 1399, 1431, 329, 442, 1434, 1645, 1436, 1437, 1438, 1439, 1440, 1133, 1442, 277, 1444, 1445, 1602, 1447, 1448, 1208, 1450, 2039, 1452, 2178, 1454, 1455, 1456, 1457, 303, 1518, 675, 1461, 1462, 286, 1464, 1811, 1466, 1467, 194, 186, 2216, 1333, 805, 733, 1034, 1475, 2421, 1477, 2158, 1089, 1480, 1481, 1482, 2221, 1426, 1485, 1486, 1487, 1488, 1489, 1863, 2530, 1492, 1493, 731, 1397, 1496, 1497, 204, 1465, 1463, 343, 1502, 1503, 1504, 1505, 99, 1500, 1508, 1474, 1510, 1511, 1512, 1513, 1514, 1515, 1516, 1517, 144, 1519, 1520, 551, 1614, 38, 2315, 711, 1527, 1484, 1528, 820, 1530, 1531, 1532, 12, 1534, 1234, 48, 1537, 1538, 1539, 1540, 1541, 348, 1269, 393, 33, 1546, 1360, 1584, 1549, 1522, 1551, 531, 1553, 1554, 764, 1556, 1557, 2013, 139, 1560, 1561, 1562, 1563, 1564, 2089, 1566, 1567, 1898, 1569, 1611, 1571, 1572, 2241, 1524, 1693, 1576, 1577, 1578, 1579, 721, 1581, 1582, 717, 1634, 1585, 842, 1587, 1421, 387, 1574, 1591, 381, 238, 684, 2416, 1596, 1525, 478, 1599, 1600, 1529, 924, 521, 1604, 1597, 1606, 806, 1732, 2225, 1590, 867, 135, 1613, 1608, 1615, 1616, 1617, 193, 1619, 1620, 1621, 1140, 1623, 1349, 1625, 1626, 763, 1628, 1629, 1630, 1631, 1632, 1318, 1526, 1635, 1636, 1637, 1638, 1908, 1640, 1946, 1642, 1643, 1644, 1441, 385, 1647, 1648, 1649, 1650, 1550, 1783, 1692, 1702, 1763, 697, 1657, 1658, 1659, 590, 1716, 2094, 1096, 1425, 1665, 1666, 1667, 1662, 1669, 1670, 1671, 1672, 1930, 1674, 1675, 1676, 1302, 615, 1679, 1680, 1681, 509, 1651, 1684, 645, 1022, 2249, 1688, 1689, 2183, 1691, 1736, 1877, 1694, 1695, 1696, 2017, 802, 1818, 1320, 345, 1430, 1837, 1704, 1705, 1412, 1801, 1708, 2155, 1710, 1711, 1712, 1713, 1714, 104, 1685, 1717, 1130, 1719, 2510, 1721, 2090, 1723, 1724, 1725, 2127, 2049, 1728, 2476, 73, 1731, 1707, 79, 1734, 2393, 1668, 1737, 1738, 1739, 1740, 1993, 1742, 1743, 60, 1654, 1746, 1747, 1748, 1749, 2101, 1751, 1752, 1753, 1754, 571, 1956, 1757, 199, 1759, 1760, 855, 1762, 1655, 2163, 1907, 1766, 1767, 1768, 1769, 1770, 1771, 1772, 232, 1774, 1775, 1776, 1777, 1395, 2232, 1789, 1861, 2350, 1836, 1784, 1792, 1786, 2143, 1788, 1810, 1356, 1791, 609, 1793, 1794, 1134, 1796, 2501, 1798, 1070, 1800, 1653, 2088, 1803, 1804, 2265, 1014, 1807, 1808, 1809, 1778, 1342, 1812, 187, 1814, 164, 1323, 296, 1699, 861, 1820, 1821, 1822, 1823, 1824, 1825, 1826, 1827, 1828, 1829, 1830, 1851, 1832, 1605, 1834, 2368, 1865, 2207, 1870, 1400, 1840, 308, 967, 1843, 1844, 1845, 1641, 1847, 1805, 407, 2271, 1831, 1852, 1853, 1901, 2516, 2481, 582, 2536, 1859, 2103, 1781, 1862, 1490, 1864, 1661, 1866, 1854, 1992, 1869, 718, 2028, 1872, 1873, 1874, 1875, 2059, 1575, 1878, 198, 1055, 1881, 1882, 1883, 2340, 1744, 1886, 1887, 2061, 2120, 350, 753, 1892, 1782, 1894, 1895, 1896, 1588, 1568, 1899, 1900, 1893, 1902, 1903, 1935, 1906, 2015, 1952, 1924, 1270, 1978, 2002, 1912, 1913, 1942, 2448, 1603, 676, 1501, 1050, 1920, 430, 1922, 1923, 1639, 1925, 1926, 223, 1928, 1929, 1673, 607, 984, 1933, 1958, 949, 1905, 1937, 1938, 1939, 397, 1941, 1909, 1943, 1944, 1945, 1846, 1947, 1948, 1949, 1950, 1951, 1765, 1953, 1954, 1955, 1756, 908, 1936, 1959, 1960, 1380, 1962, 1934, 1964, 1586, 1966, 1967, 1963, 1910, 1970, 1971, 1100, 1973, 1974, 1975, 2047, 2395, 1294, 1979, 177, 1981, 1982, 1983, 1984, 1985, 2435, 1987, 1988, 1921, 1990, 629, 1868, 1741, 72, 1995, 2129, 1997, 300, 1999, 1110, 1062, 1911, 771, 2004, 2005, 2006, 2007, 2377, 1384, 1682, 2011, 2012, 1558, 2014, 1986, 2016, 978, 2018, 510, 2020, 2133, 28, 2023, 2024, 2025, 2026, 871, 1871, 1478, 2202, 1506, 2075, 2151, 2034, 2035, 2036, 1115, 2038, 1451, 2392, 420, 2042, 2043, 2044, 2045, 2046, 520, 2048, 597, 2050, 2051, 2052, 2053, 2268, 768, 2056, 2057, 2058, 1876, 2060, 2041, 2062, 730, 2064, 2065, 2066, 2209, 2068, 2069, 2070, 2071, 2492, 2073, 1706, 2137, 2076, 1233, 2078, 2079, 2080, 21, 2082, 2083, 161, 2085, 2086, 2087, 1802, 1570, 171, 2121, 2092, 2093, 710, 2095, 589, 2097, 2098, 2099, 2100, 2112, 2102, 1860, 2196, 2105, 851, 2107, 2108, 1216, 2110, 1750, 2030, 2113, 2307, 2428, 89, 2117, 2118, 2119, 2356, 1888, 2122, 2123, 2124, 2125, 2126, 1726, 2128, 1727, 2130, 2131, 2132, 2021, 1709, 2135, 191, 1124, 2138, 2139, 2140, 1159, 2142, 1787, 834, 530, 2146, 2147, 621, 2149, 2150, 2033, 664, 2153, 371, 2031, 2156, 2157, 2220, 2231, 2029, 1314, 2162, 1764, 873, 2165, 2166, 2491, 2168, 2348, 2452, 2171, 258, 2173, 2174, 1187, 2176, 1835, 1273, 2179, 1536, 466, 2182, 2189, 2184, 2185, 2186, 976, 2188, 2200, 1622, 202, 654, 2193, 2194, 2195, 2260, 2197, 2198, 2199, 2277, 2201, 2091, 1385, 2234, 2205, 663, 1703, 2208, 862, 2210, 2276, 2212, 2242, 2214, 506, 1083, 2217, 70, 2219, 2266, 1483, 2222, 424, 2224, 1609, 2226, 2227, 2228, 2229, 2230, 2328, 845, 2116, 1008, 2235, 2236, 897, 2238, 2239, 347, 647, 1071, 2243, 2244, 2245, 2246, 2247, 82, 1610, 2250, 2251, 907, 2253, 2254, 2255, 2256, 2257, 2258, 2233, 2211, 2261, 2262, 2263, 2264, 1849, 2160, 2267, 2104, 2269, 2270, 1850, 2272, 2273, 22, 2275, 951, 463, 2289, 2279, 1690, 2369, 456, 2532, 2375, 2385, 2074, 2287, 2444, 1879, 2290, 2291, 2292, 2293, 2282, 2473, 1042, 2297, 2394, 2299, 2300, 2301, 2302, 2303, 2304, 2335, 2306, 2114, 529, 1880, 2310, 2311, 2312, 1595, 2314, 1146, 2316, 2281, 464, 2319, 2373, 2321, 2322, 2323, 2324, 2325, 2326, 2327, 2381, 2278, 801, 2331, 1932, 1040, 2334, 2317, 1009, 2337, 2338, 1103, 1884, 2341, 2342, 2343, 2344, 906, 2346, 2347, 2320, 2349, 1867, 2351, 2352, 1521, 2354, 1220, 1889, 2357, 1104, 337, 922, 2361, 458, 2363, 2364, 2365, 2366, 2367, 2177, 2402, 1065, 1254, 101, 2284, 267, 2169, 2376, 2329, 2378, 901, 2380, 2280, 425, 2283, 2384, 2309, 2386, 954, 878, 2389, 594, 2391, 2040, 1160, 2294, 1131, 732, 2285, 2398, 2399, 2400, 2359, 2401, 2403, 2404, 2405, 2406, 2407, 2387, 50, 1469, 2411, 2471, 2528, 2383, 1729, 1147, 2439, 2469, 2438, 2414, 1573, 2170, 433, 601, 2422, 2426, 2313, 2115, 2429, 2430, 2431, 2432, 2433, 2434, 604, 2436, 2390, 2425, 2417, 2440, 2441, 2442, 2443, 2288, 2535, 693, 2447, 1915, 600, 2450, 2451, 2464, 2453, 2454, 2455, 2456, 2457, 2458, 2459, 1279, 702, 2462, 2463, 2419, 2465, 2466, 2467, 2468, 2418, 2515, 671, 2472, 1449, 2474, 2475, 2470, 2477, 2478, 2479, 2480, 1856, 2482, 2483, 2484, 1389, 2486, 572, 143, 2489, 2490, 2167, 2072, 2493, 2494, 2495, 699, 2497, 2498, 2427, 1379, 1797, 185, 2503, 2504, 2505, 1199, 2507, 2508, 2509, 1720, 2511, 2534, 119, 720, 2415, 766, 452, 2518, 2519, 2520, 2521, 2522, 2523, 2524, 2525, 2526, 1476, 2413, 2529, 2485, 2531, 2538, 307, 2423, 2420, 1858, 2537, 1855, 2539, 2540, 2541]

ss_tweet=list(ss_tweet)
ss_tweet=ss_tweet[1:]


#ss_tweet.append(len(tweet_list))
ss_tweet.append(2541)


borderTweet=ss_tweet

a=[]
b=[]
j=0
i=0
for I in borderTweet:
    while i<I:
        #a.append(Best_cut_com_tweet[i])
        b.append(j)
        i+=1
    j+=1


#tweet_file='C:/Users/Administrator/Desktop/tempResult3.txt'
#f=open(tweet_file)
#g=open('C:/Users/Administrator/Desktop/tweet_file_after.txt','w')


classList=[]
for i in range(len(Best_cut_com_tweet)):
    classList.append(b[Best_cut_com_tweet.index(i+1)])



#画每个话题的频率走势图

n = 50

dividid_fifty=[l[i:i + n] for i in range(0, len(Best_cut_com_tweet), n)] #每五十个一组，统计其中每个话题的频率

l=len(dividid_fifty)

freList=[]

freList_temp=[]

for i in range(l):
    for j in range(20):
        freList_temp.append(dividid_fifty.count(j)/n)
    freList.append(freList_temp)

for i in range(l):
    plt.figure(i+1)
    fre_first=[freList[x][i] for x in range(n)]
    first=plt.plot(fre_first,l)
    plt.show()
    

# 稳定性验证实验：未进行

#进行若干次分组实验，每组实验与上一次分组的结果进行对比，看变化情况

'''
d#代表本次分类列表
b#代表上次分类列表
simCount=0
l=len(b)#推文的个数
for i in range(len(b)):
    if b[i]==d[i]:
        simCount+=1


print('本次分类的稳定性为%：f'%(simCount/l))

'''

    '''
    j=0
    for tweet in f:
        if j in a:
            inDex=a.index(j)
            #c=b.[inDex]
            classList.append([b[index]])
        else:
            classList.append(0)
        #g.write(str(c)+' 'tweet)
    '''
    '''
    a=[0,0,0,0,0,0]
    b='123'
    a[6-len(b):]
    list(b)
    a.extend(b)
    ''.join(map(str,c))
    '''
