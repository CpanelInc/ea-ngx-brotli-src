# ea-ngx-brotli-src

This is a “source-ball” package (ZC-7806) needed to compile brotli modules for  `ea-nginx` (enabled via `ea-nginx-brotli`).

The other option was to bundle it in `ea-nginx-brotli` or `ea-nginx` but then:
* users would have the source on their servers for no reason
* it would mean `ea-nginx` would have multiple sources in one repo whish is impossible to keep up to date
   * this is why we came up with the idea of source-ball packages in the first place
