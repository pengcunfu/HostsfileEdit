<template>
  <div class="home">
    <!-- Hero Section -->
    <section class="hero">
      <div class="container">
        <div class="hero-content">
          <div class="hero-text fade-in-up">
            <h1 class="hero-title">
              专业的<span class="text-gradient">Hosts文件编辑工具</span>
            </h1>
            <p class="hero-description">
              基于PySide6的Windows系统hosts文件可视化编辑工具，提供友好的图形界面来管理系统hosts文件，支持添加、修改、删除hosts条目。
            </p>
            <div class="hero-actions">
              <router-link to="/download" class="btn btn-primary">
                <svg class="icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                </svg>
                立即下载
              </router-link>
              <router-link to="/features" class="btn btn-secondary">
                查看功能
              </router-link>
            </div>
          </div>
          <div class="hero-image fade-in-up">
            <div class="app-preview">
              <img src="/main.png" alt="Hosts文件编辑工具界面截图" class="app-screenshot" />
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Features Overview -->
    <section class="features-overview">
      <div class="container">
        <div class="section-header text-center">
          <h2>为什么选择我们的工具？</h2>
          <p>简单易用的界面，强大的功能，让hosts文件管理变得轻松</p>
        </div>
        
        <div class="grid grid-3">
          <div class="feature-card card">
            <div class="feature-icon">
              <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
              </svg>
            </div>
            <h3>可视化编辑</h3>
            <p>直观的图形界面，告别命令行编辑，让hosts文件管理变得简单直观。</p>
          </div>
          
          <div class="feature-card card">
            <div class="feature-icon">
              <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 100 4m0-4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 100 4m0-4v2m0-6V4" />
              </svg>
            </div>
            <h3>双重编辑模式</h3>
            <p>支持文本编辑和按条编辑两种模式，满足不同用户的使用习惯。</p>
          </div>
          
          <div class="feature-card card">
            <div class="feature-icon">
              <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
              </svg>
            </div>
            <h3>安全可靠</h3>
            <p>自动权限检测，安全的文件操作，确保系统稳定性和数据安全。</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Usage Stats -->
    <section class="stats">
      <div class="container">
        <div class="stats-grid">
          <div class="stat-item">
            <div class="stat-number">10K+</div>
            <div class="stat-label">活跃用户</div>
          </div>
          <div class="stat-item">
            <div class="stat-number">99.9%</div>
            <div class="stat-label">稳定运行</div>
          </div>
          <div class="stat-item">
            <div class="stat-number">24/7</div>
            <div class="stat-label">技术支持</div>
          </div>
          <div class="stat-item">
            <div class="stat-number">免费</div>
            <div class="stat-label">开源使用</div>
          </div>
        </div>
      </div>
    </section>

    <!-- Quick Start -->
    <section class="quick-start">
      <div class="container">
        <div class="section-header text-center">
          <h2>快速开始</h2>
          <p>三步即可开始使用hosts文件编辑工具</p>
        </div>
        
        <div class="steps">
          <div class="step">
            <div class="step-number">1</div>
            <div class="step-content">
              <h3>下载安装</h3>
              <p>下载最新版本的hosts文件编辑工具，无需复杂安装过程</p>
            </div>
          </div>
          
          <div class="step">
            <div class="step-number">2</div>
            <div class="step-content">
              <h3>管理员运行</h3>
              <p>右键选择"以管理员身份运行"，确保有足够权限修改hosts文件</p>
            </div>
          </div>
          
          <div class="step">
            <div class="step-number">3</div>
            <div class="step-content">
              <h3>开始编辑</h3>
              <p>使用直观的界面添加、修改或删除hosts条目，一键保存生效</p>
            </div>
          </div>
        </div>
      </div>
    </section>


  </div>
</template>

<script>
export default {
  name: 'Home'
}
</script>

<style scoped>
/* Hero Section */
.hero {
  background: linear-gradient(135deg, #1f2937 0%, #374151 100%);
  color: white;
  padding: 80px 0;
  overflow: hidden;
}

.hero-content {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 48px;
  align-items: center;
}

.hero-title {
  font-size: 48px;
  font-weight: 800;
  line-height: 1.2;
  margin-bottom: 24px;
}

.hero-description {
  font-size: 20px;
  line-height: 1.6;
  margin-bottom: 32px;
  opacity: 0.9;
}

.hero-actions {
  display: flex;
  gap: 16px;
  flex-wrap: wrap;
}

.app-preview {
  perspective: 1000px;
}

.app-screenshot {
  width: 100%;
  max-width: 600px;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
  transform: rotateY(-5deg) rotateX(5deg);
  transition: transform 0.3s ease;
  border: 4px solid white;
}

.app-screenshot:hover {
  transform: rotateY(-2deg) rotateX(2deg);
}

/* Features Overview */
.features-overview {
  padding: 80px 0;
  background: #f9fafb;
}

.section-header {
  margin-bottom: 64px;
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

.feature-card {
  text-align: center;
}

.feature-icon {
  width: 64px;
  height: 64px;
  background: #2563eb;
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 24px;
  color: white;
}

.feature-icon svg {
  width: 32px;
  height: 32px;
}

.feature-card h3 {
  font-size: 24px;
  font-weight: 600;
  margin-bottom: 16px;
  color: #1f2937;
}

.feature-card p {
  color: #6b7280;
  line-height: 1.6;
}

/* Stats */
.stats {
  padding: 80px 0;
  background: #f9fafb;
  color: #1f2937;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 48px;
  text-align: center;
}

.stat-number {
  font-size: 48px;
  font-weight: 800;
  margin-bottom: 8px;
  color: #2563eb;
}

.stat-label {
  font-size: 18px;
  color: #6b7280;
}

/* Quick Start */
.quick-start {
  padding: 80px 0;
}

.steps {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 48px;
  margin-top: 64px;
}

.step {
  display: flex;
  gap: 24px;
  align-items: flex-start;
}

.step-number {
  width: 48px;
  height: 48px;
  background: #2563eb;
  color: white;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 20px;
  flex-shrink: 0;
}

.step-content h3 {
  font-size: 24px;
  font-weight: 600;
  margin-bottom: 12px;
  color: #1f2937;
}

.step-content p {
  color: #6b7280;
  line-height: 1.6;
}

/* CTA */
.cta {
  padding: 80px 0;
  background: linear-gradient(135deg, #1f2937 0%, #374151 100%);
  color: white;
}

.cta-content h2 {
  font-size: 36px;
  font-weight: 700;
  margin-bottom: 16px;
}

.cta-content p {
  font-size: 18px;
  margin-bottom: 32px;
  opacity: 0.9;
}

/* 响应式设计 */
@media (max-width: 768px) {
  .hero {
    padding: 60px 0;
  }
  
  .hero-content {
    grid-template-columns: 1fr;
    gap: 32px;
    text-align: center;
  }
  
  .hero-title {
    font-size: 36px;
  }
  
  .hero-description {
    font-size: 18px;
  }
  
  .app-window {
    transform: none;
  }
  
  .features-overview,
  .quick-start,
  .stats,
  .cta {
    padding: 60px 0;
  }
  
  .section-header h2 {
    font-size: 28px;
  }
  
  .steps {
    gap: 32px;
  }
  
  .step {
    flex-direction: column;
    text-align: center;
  }
}
</style>
