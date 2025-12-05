<template>
  <div class="download">
    <!-- Hero Section -->
    <section class="download-hero">
      <div class="container">
        <div class="hero-content text-center">
          <h1 class="hero-title">下载 Hosts文件编辑工具</h1>
          <p class="hero-description">
            免费下载最新版本，开始轻松管理你的hosts文件
          </p>
          <div class="version-info">
            <span class="version">v2.0.0</span>
            <span class="release-date">发布于 2025年1月25日</span>
          </div>
        </div>
      </div>
    </section>

    <!-- Download Options -->
    <section class="download-options">
      <div class="container">
        <div class="download-cards">
          <!-- 主要下载 -->
          <div class="download-card primary">
            <div class="card-header">
              <div class="download-icon">
                <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                </svg>
              </div>
              <h3>推荐下载</h3>
              <p>包含完整功能的独立可执行文件</p>
            </div>
            <div class="card-content">
              <div class="file-info">
                <div class="file-name">HostsFileEditor-v2.0.0.exe</div>
                <div class="file-size">约 25 MB</div>
                <div class="file-desc">Windows 7/8/10/11 兼容</div>
              </div>
              <button class="btn btn-primary download-btn" @click="downloadFile('exe')">
                <svg class="icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 10v6m0 0l-3-3m3 3l3-3" />
                </svg>
                立即下载
              </button>
            </div>
          </div>

          <!-- 源码下载 -->
          <div class="download-card">
            <div class="card-header">
              <div class="download-icon">
                <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4" />
                </svg>
              </div>
              <h3>源码下载</h3>
              <p>适合开发者和高级用户</p>
            </div>
            <div class="card-content">
              <div class="file-info">
                <div class="file-name">HostsFileEditor-Source.zip</div>
                <div class="file-size">约 2 MB</div>
                <div class="file-desc">需要Python 3.7+环境</div>
              </div>
              <button class="btn btn-secondary download-btn" @click="downloadFile('source')">
                <svg class="icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 10v6m0 0l-3-3m3 3l3-3" />
                </svg>
                下载源码
              </button>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- System Requirements -->
    <section class="requirements">
      <div class="container">
        <div class="section-header text-center">
          <h2>系统要求</h2>
          <p>确保你的系统满足以下最低要求</p>
        </div>
        
        <div class="requirements-grid">
          <div class="requirement-item">
            <div class="req-icon">
              <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.75 17L9 20l-1 1h8l-1-1-.75-3M3 13h18M5 17h14a2 2 0 002-2V5a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
              </svg>
            </div>
            <h4>操作系统</h4>
            <ul>
              <li>Windows 7 SP1 或更高版本</li>
              <li>Windows 8/8.1</li>
              <li>Windows 10</li>
              <li>Windows 11</li>
            </ul>
          </div>

          <div class="requirement-item">
            <div class="req-icon">
              <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
              </svg>
            </div>
            <h4>硬件要求</h4>
            <ul>
              <li>内存：至少 512 MB RAM</li>
              <li>磁盘空间：50 MB 可用空间</li>
              <li>处理器：任何x86/x64处理器</li>
            </ul>
          </div>

          <div class="requirement-item">
            <div class="req-icon">
              <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
              </svg>
            </div>
            <h4>权限要求</h4>
            <ul>
              <li>管理员权限（必须）</li>
              <li>文件系统读写权限</li>
              <li>网络访问权限（可选）</li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <!-- Installation Guide -->
    <section class="installation">
      <div class="container">
        <div class="section-header text-center">
          <h2>安装指南</h2>
          <p>按照以下步骤快速安装和使用</p>
        </div>

        <div class="install-steps">
          <!-- 可执行文件安装 -->
          <div class="install-method">
            <h3>
              <svg class="method-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
              </svg>
              可执行文件安装（推荐）
            </h3>
            
            <div class="steps-list">
              <div class="step">
                <div class="step-number">1</div>
                <div class="step-content">
                  <h4>下载文件</h4>
                  <p>点击上方"立即下载"按钮，下载最新版本的可执行文件</p>
                </div>
              </div>
              
              <div class="step">
                <div class="step-number">2</div>
                <div class="step-content">
                  <h4>运行程序</h4>
                  <p>右键点击下载的文件，选择"以管理员身份运行"</p>
                </div>
              </div>
              
              <div class="step">
                <div class="step-number">3</div>
                <div class="step-content">
                  <h4>开始使用</h4>
                  <p>程序启动后会自动加载当前hosts文件，即可开始编辑</p>
                </div>
              </div>
            </div>
          </div>

          <!-- 源码安装 -->
          <div class="install-method">
            <h3>
              <svg class="method-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4" />
              </svg>
              从源码安装
            </h3>
            
            <div class="code-installation">
              <div class="code-step">
                <h4>1. 安装Python环境</h4>
                <p>确保已安装Python 3.7或更高版本</p>
                <div class="code-block">
                  <code>python --version</code>
                </div>
              </div>
              
              <div class="code-step">
                <h4>2. 安装依赖</h4>
                <p>解压源码包后，在目录中运行以下命令</p>
                <div class="code-block">
                  <code>pip install -r requirements.txt</code>
                </div>
              </div>
              
              <div class="code-step">
                <h4>3. 运行程序</h4>
                <p>以管理员身份打开命令提示符，运行</p>
                <div class="code-block">
                  <code>python main.py</code>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- FAQ -->
    <section class="faq">
      <div class="container">
        <div class="section-header text-center">
          <h2>常见问题</h2>
          <p>解答用户最关心的问题</p>
        </div>

        <div class="faq-list">
          <div class="faq-item" v-for="(faq, index) in faqs" :key="index">
            <div class="faq-question" @click="toggleFaq(index)">
              <h4>{{ faq.question }}</h4>
              <svg class="faq-icon" :class="{ active: faq.open }" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
              </svg>
            </div>
            <div class="faq-answer" :class="{ active: faq.open }">
              <p>{{ faq.answer }}</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Support -->
    <section class="support">
      <div class="container">
        <div class="support-content text-center">
          <h2>需要帮助？</h2>
          <p>如果在安装或使用过程中遇到问题，我们随时为您提供支持</p>
          <div class="support-actions">
            <button class="btn btn-primary" @click="openSupport">
              <svg class="icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z" />
              </svg>
              联系支持
            </button>
            <button class="btn btn-secondary" @click="viewDocs">
              <svg class="icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.746 0 3.332.477 4.5 1.253v13C19.832 18.477 18.246 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
              </svg>
              查看文档
            </button>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'Download',
  data() {
    return {
      faqs: [
        {
          question: '为什么必须以管理员身份运行？',
          answer: 'hosts文件位于系统目录中，修改需要管理员权限。以管理员身份运行可以确保程序有足够的权限读取和写入hosts文件。',
          open: false
        },
        {
          question: '修改hosts文件后为什么不生效？',
          answer: '修改hosts文件后，可能需要刷新DNS缓存。请以管理员身份运行命令提示符，执行 "ipconfig /flushdns" 命令，然后重启浏览器。',
          open: false
        },
        {
          question: '程序会备份原始hosts文件吗？',
          answer: '是的，程序在修改hosts文件前会自动创建备份。如果出现问题，您可以手动恢复备份文件。',
          open: false
        },
        {
          question: '支持哪些Windows版本？',
          answer: '支持Windows 7 SP1及以上版本，包括Windows 8/8.1、Windows 10和Windows 11。建议使用最新版本的Windows以获得最佳体验。',
          open: false
        },
        {
          question: '如何卸载程序？',
          answer: '这是一个绿色软件，无需安装。如果不再需要，直接删除程序文件即可。您的hosts文件不会受到影响。',
          open: false
        },
        {
          question: '程序是否免费？',
          answer: '是的，hosts文件编辑工具完全免费使用，无任何功能限制。我们致力于为用户提供优质的免费工具。',
          open: false
        }
      ]
    }
  },
  methods: {
    downloadFile(type) {
      // 模拟下载功能
      if (type === 'exe') {
        alert('开始下载可执行文件...\n\n注意：这是一个演示网站，实际下载链接需要您提供真实的文件地址。')
      } else if (type === 'source') {
        alert('开始下载源码包...\n\n注意：这是一个演示网站，实际下载链接需要您提供真实的文件地址。')
      }
    },
    toggleFaq(index) {
      this.faqs[index].open = !this.faqs[index].open
    },
    openSupport() {
      alert('联系支持功能\n\n您可以在这里添加实际的支持联系方式，如邮箱、QQ群等。')
    },
    viewDocs() {
      alert('查看文档功能\n\n您可以在这里链接到详细的使用文档或帮助页面。')
    }
  }
}
</script>

<style scoped>
/* Hero Section */
.download-hero {
  background: linear-gradient(135deg, #1f2937 0%, #374151 100%);
  color: white;
  padding: 80px 0;
}

.hero-title {
  font-size: 48px;
  font-weight: 800;
  margin-bottom: 24px;
}

.hero-description {
  font-size: 20px;
  opacity: 0.9;
  margin-bottom: 32px;
  max-width: 600px;
  margin-left: auto;
  margin-right: auto;
}

.version-info {
  display: flex;
  justify-content: center;
  gap: 24px;
  font-size: 16px;
}

.version {
  background: rgba(255, 255, 255, 0.2);
  padding: 8px 16px;
  border-radius: 20px;
  font-weight: 600;
}

.release-date {
  opacity: 0.8;
}

/* Download Options */
.download-options {
  padding: 80px 0;
}

.download-cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
  gap: 32px;
  max-width: 800px;
  margin: 0 auto;
}

.download-card {
  background: white;
  border-radius: 16px;
  padding: 32px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
  transition: all 0.3s ease;
  border: 2px solid transparent;
}

.download-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 40px rgba(0, 0, 0, 0.15);
}

.download-card.primary {
  border-color: #2563eb;
  background: linear-gradient(135deg, #f8faff, #f0f7ff);
}

.card-header {
  text-align: center;
  margin-bottom: 32px;
}

.download-icon {
  width: 64px;
  height: 64px;
  background: #2563eb;
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 16px;
  color: white;
}

.download-icon svg {
  width: 32px;
  height: 32px;
}

.card-header h3 {
  font-size: 24px;
  font-weight: 600;
  margin-bottom: 8px;
  color: #1f2937;
}

.card-header p {
  color: #6b7280;
}

.file-info {
  margin-bottom: 24px;
}

.file-name {
  font-size: 18px;
  font-weight: 600;
  color: #1f2937;
  margin-bottom: 4px;
}

.file-size {
  color: #6b7280;
  margin-bottom: 4px;
}

.file-desc {
  color: #6b7280;
  font-size: 14px;
}

.download-btn {
  width: 100%;
  justify-content: center;
}

/* Requirements */
.requirements {
  padding: 80px 0;
  background: #f9fafb;
}

.requirements-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 32px;
  margin-top: 48px;
}

.requirement-item {
  background: white;
  padding: 32px;
  border-radius: 16px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
}

.req-icon {
  width: 48px;
  height: 48px;
  background: #2563eb;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 16px;
  color: white;
}

.req-icon svg {
  width: 24px;
  height: 24px;
}

.requirement-item h4 {
  font-size: 20px;
  font-weight: 600;
  margin-bottom: 16px;
  color: #1f2937;
}

.requirement-item ul {
  list-style: none;
  padding: 0;
}

.requirement-item li {
  padding: 6px 0;
  color: #6b7280;
  position: relative;
  padding-left: 20px;
}

.requirement-item li::before {
  content: "•";
  position: absolute;
  left: 0;
  color: #2563eb;
  font-weight: bold;
}

/* Installation */
.installation {
  padding: 80px 0;
}

.install-steps {
  margin-top: 48px;
  max-width: 900px;
  margin-left: auto;
  margin-right: auto;
}

.install-method {
  margin-bottom: 64px;
  background: white;
  padding: 40px;
  border-radius: 16px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
}

.install-method h3 {
  display: flex;
  align-items: center;
  gap: 12px;
  font-size: 24px;
  font-weight: 600;
  margin-bottom: 32px;
  color: #1f2937;
}

.method-icon {
  width: 24px;
  height: 24px;
  color: #2563eb;
}

.steps-list {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.step {
  display: flex;
  gap: 20px;
  align-items: flex-start;
}

.step-number {
  width: 40px;
  height: 40px;
  background: #2563eb;
  color: white;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 600;
  flex-shrink: 0;
}

.step-content h4 {
  font-size: 18px;
  font-weight: 600;
  margin-bottom: 8px;
  color: #1f2937;
}

.step-content p {
  color: #6b7280;
  line-height: 1.6;
}

.code-installation {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.code-step h4 {
  font-size: 18px;
  font-weight: 600;
  margin-bottom: 8px;
  color: #1f2937;
}

.code-step p {
  color: #6b7280;
  margin-bottom: 12px;
}

.code-block {
  background: #1e293b;
  color: #e2e8f0;
  padding: 16px;
  border-radius: 8px;
  font-family: 'Courier New', monospace;
  font-size: 14px;
}

/* FAQ */
.faq {
  padding: 80px 0;
  background: #f9fafb;
}

.faq-list {
  max-width: 800px;
  margin: 48px auto 0;
}

.faq-item {
  background: white;
  border-radius: 12px;
  margin-bottom: 16px;
  overflow: hidden;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.08);
}

.faq-question {
  padding: 24px;
  cursor: pointer;
  display: flex;
  justify-content: space-between;
  align-items: center;
  transition: background 0.2s ease;
}

.faq-question:hover {
  background: #f9fafb;
}

.faq-question h4 {
  font-size: 18px;
  font-weight: 600;
  color: #1f2937;
  margin: 0;
}

.faq-icon {
  width: 20px;
  height: 20px;
  color: #6b7280;
  transition: transform 0.3s ease;
}

.faq-icon.active {
  transform: rotate(180deg);
}

.faq-answer {
  padding: 0 24px;
  max-height: 0;
  overflow: hidden;
  transition: all 0.3s ease;
}

.faq-answer.active {
  padding: 0 24px 24px;
  max-height: 200px;
}

.faq-answer p {
  color: #6b7280;
  line-height: 1.6;
  margin: 0;
}

/* Support */
.support {
  padding: 80px 0;
}

.support-content h2 {
  font-size: 36px;
  font-weight: 700;
  margin-bottom: 16px;
  color: #1f2937;
}

.support-content p {
  font-size: 18px;
  color: #6b7280;
  margin-bottom: 32px;
  max-width: 600px;
  margin-left: auto;
  margin-right: auto;
}

.support-actions {
  display: flex;
  gap: 16px;
  justify-content: center;
  flex-wrap: wrap;
}

/* Section Header */
.section-header {
  margin-bottom: 48px;
}

.section-header h2 {
  font-size: 36px;
  font-weight: 700;
  margin-bottom: 16px;
  color: #1f2937;
}

.section-header p {
  font-size: 18px;
  color: #6b7280;
  max-width: 600px;
  margin: 0 auto;
}

/* 响应式设计 */
@media (max-width: 768px) {
  .download-hero {
    padding: 60px 0;
  }
  
  .hero-title {
    font-size: 36px;
  }
  
  .hero-description {
    font-size: 18px;
  }
  
  .version-info {
    flex-direction: column;
    gap: 12px;
  }
  
  .download-options,
  .requirements,
  .installation,
  .faq,
  .support {
    padding: 60px 0;
  }
  
  .download-cards {
    grid-template-columns: 1fr;
  }
  
  .requirements-grid {
    grid-template-columns: 1fr;
  }
  
  .install-method {
    padding: 24px;
  }
  
  .step {
    flex-direction: column;
    text-align: center;
  }
  
  .section-header h2 {
    font-size: 28px;
  }
  
  .support-actions {
    flex-direction: column;
    align-items: center;
  }
}
</style>
