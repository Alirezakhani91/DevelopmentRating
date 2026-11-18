راه‌اندازی یک‌باره:
1) محتویات این پوشه را در یک GitHub repository آپلود کنید (فایل index.html و data.json و update_data.py و پوشه .github).
2) Settings > Pages > Deploy from a branch > main / root > Save.
3) Settings > Actions > General > Workflow permissions > Read and write permissions > Save.
4) Actions > Update Daily Market dashboard > Run workflow.
سپس داده‌ها طبق زمان‌بندی هر ۱۵ دقیقه (به صورت best-effort GitHub) به‌روزرسانی می‌شوند. صفحه مرورگر هر ۵ دقیقه فایل JSON جدید را می‌خواند.
نکته: در بارگذاری فایل‌ها از وب‌سایت GitHub دقت کنید فایل .github/workflows/update.yml با مسیر پوشه‌ای صحیح ساخته شود؛ فایل‌های ریشه را جداگانه آپلود کنید یا از Git استفاده کنید.
منبع: تب 980860521 از شیت منتشرشده.
