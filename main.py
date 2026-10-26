def checklist_progress(done, total):
    return done / total * 100

if __name__ == "__main__":
    done, total = 11, 11
    print("Hello GitHub Actions!")
    print(f"文件備妥進度：{done}/{total} ({checklist_progress(done, total):.0f}%)")
