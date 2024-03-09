def depth(args,url_dir):
    for i in  range(len(url_dir)):
        from .finger import finger_scan
        args.url = url_dir[i]
        finger_scan(args)