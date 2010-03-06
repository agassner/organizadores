<div id="footer" class="wrap">

	<div class="left-col">
		<div class="popular wrap">
			<h2><?php _e('Most Popular Articles',woothemes); ?></h2>
			<ul>
                <!-- Gets the posts with the most comments -->
				<?php popular_posts(); ?>                    
			</ul>
		</div>
	</div>
	
	<div id="subscribe" class="right-col">
		<h2><?php _e('Subscribe to RSS',woothemes); ?></h2>
		<p class="rss"><?php _e('If you enjoyed the post, make sure you subscribe to the RSS feed',woothemes); ?>.</p>
		<p>
		<a href="<?php if ( get_option('woo_feedburner_url') <> "" ) { echo get_option('woo_feedburner_url'); } else { echo get_bloginfo_rss('rss2_url'); } ?>"><?php _e('Articles',woothemes); ?></a><br />
		<a href="<?php bloginfo('comments_rss2_url'); ?>"><?php _e('Comments',woothemes); ?></a>
		</p>
	</div>
	
<div id="copyright" class="wrap">

	<div class="left-col">
		<p>&copy; <?php echo date('Y'); ?></p>
	</div>
	
	<div class="right-col">
		<p><?php _e('Powered by',woothemes); ?> WordPress. <?php _e('Design by',woothemes); ?> <a href="http://woothemes.com"><img src="<?php bloginfo('template_directory'); ?>/<?php woo_style_path(); ?>/logo-footer.jpg" width="87" height="21" alt="woo themes" /></a></p>
	</div>

</div>

</div>
<?php wp_footer(); ?>

</body>
</html>