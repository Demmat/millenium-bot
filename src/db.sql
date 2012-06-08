CREATE TABLE "cfg" (
"param"  TEXT(35) NOT NULL,
"value"  TEXT(255),
PRIMARY KEY ("param") ON CONFLICT REPLACE
)
;

CREATE UNIQUE INDEX "pk"
ON "cfg" ("param");




-- 
UPDATE "main"."cfg" SET "value"='lol' WHERE ("param"='user')