## Build a static website

```
npx quartz build --serve
```

## Push to GitHub Repo

```
npx quartz sync
```

## Publish to Cloudflare Pages

- Remove `quartz-themes` from `quartz.config.yaml` and reinstall plugins using `npx quartz plugin install --from-config`.
- Follow the instructions in [Hosting](https://quartz.jzhao.xyz/hosting#cloudflare-pages).