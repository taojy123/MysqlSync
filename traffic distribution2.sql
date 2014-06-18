/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50616
Source Host           : localhost:3306
Source Database       : test

Target Server Type    : MYSQL
Target Server Version : 50616
File Encoding         : 65001

Date: 2014-06-18 22:59:10
*/

SET FOREIGN_KEY_CHECKS=0;
-- ----------------------------
-- Table structure for `traffic distribution`
-- ----------------------------
DROP TABLE IF EXISTS `traffic distribution`;
CREATE TABLE `traffic distribution` (
  `CMID` int(11) NOT NULL,
  `SkillNum` int(11) NOT NULL,
  `MonitorTime` varchar(30) NOT NULL,
  `SkillLevel` int(11) NOT NULL,
  `VDN/AGENT` double(11,3) NOT NULL,
  `HOLD/AGENT` double(11,3) NOT NULL,
  `ABAND/AGENT` double(11,3) NOT NULL,
  `QUEUE/AGENT` double(11,3) NOT NULL,
  `AVGANS` int(255) NOT NULL,
  `AVGABAND` varchar(255) NOT NULL,
  `CreateTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`CMID`,`SkillNum`,`CreateTime`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of traffic distribution
-- ----------------------------
INSERT INTO `traffic distribution` VALUES ('1', '1201', '22:52 WED JUN 18 2014', '93', '0', '1', '0', '0', '0', '', '2014-06-18 22:54:28');
INSERT INTO `traffic distribution` VALUES ('1', '1201', '22:52 WED JUN 18 2014', '93', '2', '1', '0', '1', '0', '', '2014-06-18 22:58:01');
