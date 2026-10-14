import os
import matplotlib.pyplot as plt
import pandas as pd

os.makedirs('images', exist_ok=True)

def generate_performance_chart(jtl_path, output_png, title):
    if not os.path.exists(jtl_path):
        print(f"Không tìm thấy file: {jtl_path}")
        return
    
    # Đọc dữ liệu JTL
    df = pd.read_csv(jtl_path)
    
    plt.figure(figsize=(10, 5))
    plt.plot(df['elapsed'], color='#1f77b4', alpha=0.6, linewidth=1, label='Response Time (ms)')
    
    mean_val = df['elapsed'].mean()
    p90_val = df['elapsed'].quantile(0.90)
    
    plt.axhline(y=mean_val, color='r', linestyle='--', label=f'Average: {mean_val:.1f} ms')
    plt.axhline(y=p90_val, color='orange', linestyle=':', label=f'90th Percentile: {p90_val:.1f} ms')
    
    plt.title(title, fontsize=14, fontweight='bold')
    plt.xlabel('Request Number', fontsize=11)
    plt.ylabel('Response Time (ms)', fontsize=11)
    plt.legend(loc='upper right')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    
    plt.savefig(output_png, dpi=150)
    plt.close()
    print(f"Đã tạo thành công ảnh: {output_png}")

# Tiến hành tạo ảnh
generate_performance_chart('results_web.jtl', 'images/web_report.png', 'Web Performance Test - Response Time (10,000 Threads)')
generate_performance_chart('results_api.jtl', 'images/api_report.png', 'API Performance Test - Response Time (10,000 Threads)')