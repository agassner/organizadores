<?php
// Do not delete these lines
	if (!empty($_SERVER['SCRIPT_FILENAME']) && 'comments.php' == basename($_SERVER['SCRIPT_FILENAME']))
		die ('Please do not load this page directly. Thanks!');

	if ( post_password_required() ) { ?>
		<p class="nocomments"><?php _e('This post is password protected. Enter the password to view comments',woothemes); ?>.</p>
	<?php
		return;
	}
?>

<!-- You can start editing here. -->

<div id="comments_wrap">

<?php if ( have_comments() ) : ?>

	<h3 id="comments"><?php comments_number(__('No Comments',woothemes), __('One Comment',woothemes), __('% Comments',woothemes) );?> <?php _e('to',woothemes); ?> &#8220;<?php the_title(); ?>&#8221;</h3>

	<ol class="commentlist">
	<?php wp_list_comments('avatar_size=35&callback=custom_comment'); ?>
	</ol>    

	<div class="navigation">
		<div class="alignleft"><?php previous_comments_link() ?></div>
		<div class="alignright"><?php next_comments_link() ?></div>
		<div class="fix"></div>
	</div>
	<br />
 
<?php else : // this is displayed if there are no comments so far ?>

	<?php if ('open' == $post->comment_status) : ?>
		<!-- If comments are open, but there are no comments. -->

	 <?php else : // comments are closed ?>
		<!-- If comments are closed. -->
		<p class="nocomments"><?php _e('Comments are closed',woothemes); ?>.</p>

	<?php endif; ?>

<?php endif; ?>

</div> <!-- end #comments_wrap -->

<?php if ('open' == $post->comment_status) : ?>

<div id="respond">

<h3 class="lc"><?php comment_form_title( __('Leave a Reply',woothemes), __('Leave a Reply to %s',woothemes) ); ?></h3>
<div class="cancel-comment-reply">
	<p><small><?php cancel_comment_reply_link(); ?></small></p>
</div>

<?php if ( get_option('comment_registration') && !$user_ID ) : ?>

<p><?php _e('You must be',woothemes); ?> <a href="<?php echo get_option('siteurl'); ?>/wp-login.php?redirect_to=<?php the_permalink(); ?>"><?php _e('logged in',woothemes); ?></a> <?php _e('to post a comment.',woothemes); ?></p>

<?php else : ?>
<form action="<?php echo get_option('siteurl'); ?>/wp-comments-post.php" method="post" id="commentform">

<?php if ( $user_ID ) : ?>

<p><?php _e('Logged in as',woothemes); ?> <a href="<?php echo get_option('siteurl'); ?>/wp-admin/profile.php"><?php echo $user_identity; ?></a>. <a href="<?php echo get_option('siteurl'); ?>/wp-login.php?action=logout" title="<?php _e('Log out of this account',woothemes); ?>"><?php _e('Logout &raquo;',woothemes); ?></a></p>

<?php else : ?>
<label for="author"><?php _e('Username',woothemes); ?> <?php if ($req) echo  __('(required)',woothemes); ?> :<br />
<input type="text" name="author" id="author" value="<?php echo $comment_author; ?>" size="27" tabindex="1" /></label> 



<label for="email"><?php _e('Email',woothemes); ?> <?php if ($req) echo  __('(required)',woothemes); ?> :<br />
<input type="text" name="email" id="email" value="<?php echo $comment_author_email; ?>" size="27" tabindex="2" /></label> 



<label for="url"><?php _e('Web Site',woothemes); ?> :<br />
<input type="text" name="url" id="url" value="<?php echo $comment_author_url; ?>" size="27" tabindex="3" /></label> 


<?php endif; ?>

<!--<p><small><strong>XHTML:</strong> You can use these tags: <?php echo allowed_tags(); ?></small></p>-->


<label for="comment"><?php _e('Comment',woothemes); ?> :<br /></label> 
<textarea name="comment" id="comment" cols="50" rows="8" tabindex="4"></textarea>



<input name="submit" type="submit" id="submit" tabindex="5" value="<?php _e('Submit',woothemes); ?>" class="sb" />



<input type="hidden" name="comment_post_ID" value="<?php echo $id; ?>" />
<?php comment_id_fields(); ?>
<?php do_action('comment_form', $post->ID); ?>

</form>

<?php endif; // If logged in ?>

<div class="fix"></div>
</div> <!-- end #respond -->

<?php endif; // if you delete this the sky will fall on your head ?>
