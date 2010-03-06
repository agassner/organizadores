<?php get_header(); ?>

	<div class="wrap background">
		
		<div id="content" class="left-col wrap">
		
		<?php if (have_posts()) : ?>
		<?php while (have_posts()) : the_post(); ?>
		
		<!--- Post Starts -->
		
			<div class="post wrap">
			
				<div class="post-meta left-col">
					<h3 class="wrap"><span class="month"><?php the_time('M'); ?><span class="year"><?php the_time('o'); ?></span></span><span class="day"><?php the_time('d'); ?></span></h3>
					<h4 class="author"><?php the_author_posts_link(); ?></h4>
					<h4 class="comments"><a href="<?php comments_link(); ?>"><?php comments_number('0','1','%'); ?></a></h4>
				</div>
				
				<div class="post-content right-col">
					<h2><a href="<?php the_permalink() ?>" rel="bookmark" title="<?php the_title(); ?>"><?php the_title(); ?></a></h2>
					
					<?php woo_get_image('image',get_option('woo_thumb_width'),get_option('woo_thumb_height'),'thumb alignleft'); ?>
					
					<?php
					if ( get_option('woo_content_home') == "true" ) 
						the_content('[...]'); 
					else 
						the_excerpt(); 
					?>
					
				</div>
				
			</div>
			
			<!--- Post Ends -->
			
			<?php endwhile; ?>
			
			<div class="more_posts">
				<h2><?php next_posts_link(__('&laquo; Older Entries',woothemes)) ?> &nbsp; <?php previous_posts_link (__('Recent Entries &raquo;',woothemes)) ?></h2>
			</div>
			
			<?php endif; ?>
			
		</div>
		
		<?php get_sidebar(); ?>
		
	</div>
	
</div>
	
<?php get_footer(); ?>