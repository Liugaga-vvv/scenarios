# Log Parsing

`access.log` is a log file that records access requests from others, each line representing a single access. The format of this file is `uri used_time`. Here are some examples of log files below.

```bash
/create/order 0.10
/create/order 2.88
/query/order/info 1.55
/service/pricing 0.45
...
```

Our challenge is to analyze this log file and the statistics of each uri request count.
