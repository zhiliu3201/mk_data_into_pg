#!/bin/bash
psql -h quad111 -p 5444 -d xsbench4 -c "delete from lineitem;"

scp lineitem_4.tbl quad114:/home/liuzhi/
scp lineitem_3.tbl quad113:/home/liuzhi/
scp lineitem_2.tbl quad112:/home/liuzhi/
scp lineitem_1.tbl quad111:/home/liuzhi/
psql -h quad114 -p 5444 -d xsbench4 -c "copy lineitem from '/home/liuzhi/lineitem_4.tbl' with delimiter as '|';"
psql -h quad113 -p 5444 -d xsbench4 -c "copy lineitem from '/home/liuzhi/lineitem_3.tbl' with delimiter as '|';"
psql -h quad112 -p 5444 -d xsbench4 -c "copy lineitem from '/home/liuzhi/lineitem_2.tbl' with delimiter as '|';"
psql -h quad111 -p 5444 -d xsbench4 -c "copy lineitem from '/home/liuzhi/lineitem_1.tbl' with delimiter as '|';"
