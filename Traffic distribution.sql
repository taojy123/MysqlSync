/*
Navicat MySQL Data Transfer

Source Server         : 测试mysql
Source Server Version : 50537
Source Host           : 10.253.25.212:3306
Source Database       : CCBaseDB

Target Server Type    : MYSQL
Target Server Version : 50537
File Encoding         : 65001

Date: 2014-07-26 12:23:02
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `Traffic distribution`
-- ----------------------------
DROP TABLE IF EXISTS `Traffic distribution`;
CREATE TABLE `Traffic distribution` (
  `CMID` int(11) NOT NULL,
  `SkillNum` int(11) NOT NULL,
  `MonitorTime` varchar(30) NOT NULL,
  `SkillLevel` int(11) NOT NULL,
  `VDN/AGENT` double(11,0) NOT NULL,
  `HOLD/AGENT` double(11,0) NOT NULL,
  `ABAND/AGENT` double(11,0) NOT NULL,
  `QUEUE/AGENT` double(11,0) NOT NULL,
  `AVGANS` int(255) NOT NULL,
  `AVGABAND` varchar(255) NOT NULL,
  `CreateTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`CMID`,`SkillNum`,`CreateTime`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of Traffic distribution
-- ----------------------------
