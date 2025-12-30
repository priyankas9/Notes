10.19.2024 saturday
query used for building layer  - joins building and building business table 👍

SELECT

    b.*,

    bb.*

FROM

    buildings b

JOIN

    buildings_business bb

ON

    b.bin=bb.bin;
