test:
	for d in ./*/ ; do -execdir cd "$d" && ls; done

