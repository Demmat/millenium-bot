/*
Navicat SQLite Data Transfer

Source Server         : mille
Source Server Version : 30706
Source Host           : :0

Target Server Type    : SQLite
Target Server Version : 30706
File Encoding         : 65001

Date: 2012-06-08 19:28:28
*/

PRAGMA foreign_keys = OFF;

-- ----------------------------
-- Table structure for "main"."cfg"
-- ----------------------------
DROP TABLE "main"."cfg";
CREATE TABLE "cfg" (
"param"  TEXT(35) NOT NULL,
"value"  TEXT(255),
PRIMARY KEY ("param") ON CONFLICT REPLACE
);

-- ----------------------------
-- Records of cfg
-- ----------------------------
INSERT INTO "main"."cfg" VALUES ('user', '_');
INSERT INTO "main"."cfg" VALUES ('passw', null);
INSERT INTO "main"."cfg" VALUES ('User-Agent', 'Mozilla/5.0');
INSERT INTO "main"."cfg" VALUES ('lastrun', '08/06/2012 19:20');

-- ----------------------------
-- Table structure for "main"."Top"
-- ----------------------------
DROP TABLE "main"."Top";
CREATE TABLE "Top" (
"VoteId"  INTEGER NOT NULL,
"Nom"  TEXT,
"Url"  TEXT,
PRIMARY KEY ("VoteId") ON CONFLICT REPLACE
);

-- ----------------------------
-- Records of Top
-- ----------------------------
INSERT INTO "main"."Top" VALUES (3, 'RPG-Millenium', 'http://www.rpg-paradize.com/?page=vote&vote=5846');
INSERT INTO "main"."Top" VALUES (4, 'RPG-Hovercraft', 'http://www.rpg-paradize.com/?page=vote&vote=32321');

-- ----------------------------
-- Indexes structure for table cfg
-- ----------------------------
CREATE UNIQUE INDEX "main"."pk_param"
ON "cfg" ("param" ASC);

-- ----------------------------
-- Indexes structure for table Top
-- ----------------------------
CREATE UNIQUE INDEX "main"."pk_Voteid"
ON "Top" ("VoteId" ASC);
