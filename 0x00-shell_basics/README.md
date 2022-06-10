# Shell, basics

<div>
    <h2>
      About <span class="text-primary">Bash</span> projects
    </h2>
    <p>
      </p><p>Unless stated, all your projects will be auto-corrected with Ubuntu 20.04 LTS.</p>
    <p></p>
</div>

<div class="panel panel-default" id="project-description">
  <div class="panel-body">
    <p><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/205/image.jpg" alt="" style=""></p>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="http://linuxcommand.org/lc3_lts0010.php" title="What Is &quot;The Shell&quot;?" target="_blank">What Is “The Shell”?</a> </li>
<li><a href="http://linuxcommand.org/lc3_lts0020.php" title="Navigation" target="_blank">Navigation</a> </li>
<li><a href="http://linuxcommand.org/lc3_lts0030.php" title="Looking Around" target="_blank">Looking Around</a> </li>
<li><a href="http://linuxcommand.org/lc3_lts0040.php" title="A Guided Tour" target="_blank">A Guided Tour</a> </li>
<li><a href="http://linuxcommand.org/lc3_lts0050.php" title="Manipulating Files" target="_blank">Manipulating Files</a> </li>
<li><a href="http://linuxcommand.org/lc3_lts0060.php" title="Working With Commands" target="_blank">Working With Commands</a> </li>
<li><a href="http://linuxcommand.org/lc3_man_pages/man1.html" title="Reading Man pages" target="_blank">Reading Man pages</a> </li>
<li><a href="https://www.howtogeek.com/howto/ubuntu/keyboard-shortcuts-for-bash-command-shell-for-ubuntu-debian-suse-redhat-linux-etc/" title="Keyboard shortcuts for Bash" target="_blank">Keyboard shortcuts for Bash</a> </li>
<li><a href="https://wiki.ubuntu.com/LTS" target="_blank">LTS</a></li>
<li><a href="https://en.wikipedia.org/wiki/Shebang_%28Unix%29" title="Shebang" target="_blank">Shebang</a> </li>
</ul>

<p><strong>man or help</strong>:</p>

<ul>
<li><code>cd</code></li>
<li><code>ls</code></li>
<li><code>pwd</code></li>
<li><code>less</code></li>
<li><code>file</code></li>
<li><code>ln</code></li>
<li><code>cp</code></li>
<li><code>mv</code></li>
<li><code>rm</code></li>
<li><code>mkdir</code></li>
<li><code>type</code></li>
<li><code>which</code></li>
<li><code>help</code></li>
<li><code>man</code></li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="https://fs.blog/feynman-learning-technique/" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>What does RTFM mean?</li>
<li>What is a Shebang</li>
</ul>

<h3>What is the Shell</h3>

<ul>
<li>What is the shell</li>
<li>What is the difference between a terminal and a shell</li>
<li>What is the shell prompt</li>
<li>How to use the history (the basics)</li>
</ul>

<h3>Navigation</h3>

<ul>
<li>What do the commands or built-ins <code>cd</code>, <code>pwd</code>, <code>ls</code> do </li>
<li>How to navigate the filesystem</li>
<li>What are the . and .. directories</li>
<li>What is the working directory, how to print it and how to change it</li>
<li>What is the root directory</li>
<li>What is the home directory, and how to go there</li>
<li>What is the difference between the root directory and the home directory of the user root</li>
<li>What are the characteristics of hidden files and how to list them</li>
<li>What does the command <code>cd -</code> do</li>
</ul>

<h3>Looking Around</h3>

<ul>
<li>What do the commands <code>ls</code>, <code>less</code>, <code>file</code> do</li>
<li>How do you use options and arguments with commands</li>
<li>Understand the ls long format and how to display it</li>
<li><a href="http://linuxcommand.org/lc3_lts0040.php" title="A Guided Tour" target="_blank">A Guided Tour</a></li>
<li>What does the <code>ln</code> command do</li>
<li>What do you find in the most common/important directories</li>
<li>What is a symbolic link</li>
<li>What is a hard link</li>
<li>What is the difference between a hard link and a symbolic link</li>
</ul>

<h3>Manipulating Files</h3>

<ul>
<li>What do the commands <code>cp</code>, <code>mv</code>, <code>rm</code>, <code>mkdir</code> do</li>
<li>What are wildcards and how do they work</li>
<li>How to use wildcards</li>
</ul>

<h3>Working with Commands</h3>

<ul>
<li>What do <code>type</code>, <code>which</code>, <code>help</code>, <code>man</code> commands do</li>
<li>What are the different kinds of commands</li>
<li>What is an alias</li>
<li>When do you use the command help instead of man</li>
</ul>

<h3>Reading Man Pages</h3>

<ul>
<li>How to read a man page</li>
<li>What are man page sections</li>
<li>What are the section numbers for User commands, System calls and Library functions</li>
</ul>

<h3>Keyboard Shortcuts for Bash</h3>

<ul>
<li>Common shortcuts for Bash</li>
</ul>

<h3>LTS</h3>

<ul>
<li>What does <code>LTS</code> mean?</li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your scripts will be tested on Ubuntu 20.04 LTS</li>
<li>All your scripts should be exactly two lines long (<code>$ wc -l file</code> should print 2)</li>
<li>All your files should end with a new line (<a href="http://unix.stackexchange.com/questions/18743/whats-the-point-in-adding-a-new-line-to-the-end-of-a-file/18789">why?</a>)</li>
<li>The first line of all your files should be exactly <code>#!/bin/bash</code></li>
<li>A <code>README.md</code> file at the root of the repo, containing a description of the repository</li>
<li>A <code>README.md</code> file, at the root of the folder of <em>this</em> project, describing what each script is doing</li>
<li>You are not allowed to use backticks, <code>&amp;&amp;</code>, <code>||</code> or <code>;</code></li>
<li>All your scripts must be executable. To make your file executable, use the <code>chmod</code> command:  <code>chmod u+x file</code>. Later, we’ll learn more about how to utilize this command.</li>
</ul>

<h2>More Info</h2>

<p><i>Example of line count and first line</i></p>

<pre><code>julien@ubuntu:/tmp$ wc -l 12-file_type 
2 12-file_type
julien@ubuntu:/tmp$ head -n 1 12-file_type 
#!/bin/bash
julien@ubuntu:/tmp$ 
</code></pre>

<p>In order to test your scripts, you will need to use this command: <code>chmod u+x file</code>. We will see later what does <code>chmod</code> mean and do, but you can have a look at <code>man chmod</code> if you are curious.</p>

<p><i>Example</i></p>

<pre><code>julien@ubuntu:/tmp$ ls
12-file_type
lll
julien@ubuntu:/tmp$ ls -la lll
-rw-rw-r-- 1 julien julien 15 Sep 19 21:05 lll
julien@ubuntu:/tmp$ cat lll
#!/bin/bash
ls
julien@ubuntu:/tmp$ ls -l lll
-rw-rw-r-- 1 julien julien 15 Sep 19 21:05 lll
julien@ubuntu:/tmp$ chmod u+x lll # you do not have to understand this yet
julien@ubuntu:/tmp$ ls -l lll
-rwxrw-r-- 1 julien julien 15 Sep 19 21:05 lll
julien@ubuntu:/tmp$ ./lll
12-file_type
lll
julien@ubuntu:/tmp$ 
</code></pre>

  </div>
</div>
