import cv2, yaml, sys, pathlib, tqdm

cfg = yaml.safe_load(open("config.yaml", encoding="utf-8"))
src_pts = cv2.convexHull(
    cv2.UMat(np.array(cfg["roi"], dtype="float32"))
).get().astype("float32")  # 4×2

dst_w, dst_h = cfg["output_size"]
dst_pts = np.array([[0, 0], [dst_w, 0], [dst_w, dst_h], [0, dst_h]], dtype="float32")

M = cv2.getPerspectiveTransform(src_pts, dst_pts)

in_dir  = pathlib.Path("frames")
out_dir = pathlib.Path("minimaps"); out_dir.mkdir(exist_ok=True)

for f in tqdm.tqdm(sorted(in_dir.glob("*.jpg"))):
    img   = cv2.imread(str(f))
    warp  = cv2.warpPerspective(img, M, (dst_w, dst_h))
    out_f = out_dir / f.name
    cv2.imwrite(str(out_f), warp)
print("Done:", len(list(out_dir.glob('*.jpg'))), "images")
