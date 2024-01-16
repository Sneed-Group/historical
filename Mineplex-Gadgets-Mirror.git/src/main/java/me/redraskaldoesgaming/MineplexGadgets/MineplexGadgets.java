package me.redraskaldoesgaming.MineplexGadgets;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

import net.minecraft.server.v1_7_R3.EntityEnderPearl;

import org.bukkit.Bukkit;
import org.bukkit.ChatColor;
import org.bukkit.Color;
import org.bukkit.FireworkEffect;
import org.bukkit.FireworkEffect.Type;
import org.bukkit.Location;
import org.bukkit.Material;
import org.bukkit.Server;
import org.bukkit.Sound;
import org.bukkit.command.Command;
import org.bukkit.command.CommandSender;
import org.bukkit.enchantments.Enchantment;
import org.bukkit.entity.Bat;
import org.bukkit.entity.Creature;
import org.bukkit.entity.EnderPearl;
import org.bukkit.entity.Entity;
import org.bukkit.entity.EntityType;
import org.bukkit.entity.Firework;
import org.bukkit.entity.LivingEntity;
import org.bukkit.entity.Player;
import org.bukkit.entity.Snowball;
import org.bukkit.entity.TNTPrimed;
import org.bukkit.event.EventHandler;
import org.bukkit.event.EventPriority;
import org.bukkit.event.Listener;
import org.bukkit.event.block.Action;
import org.bukkit.event.entity.EntityDeathEvent;
import org.bukkit.event.entity.ProjectileHitEvent;
import org.bukkit.event.inventory.ClickType;
import org.bukkit.event.inventory.InventoryAction;
import org.bukkit.event.inventory.InventoryClickEvent;
import org.bukkit.event.player.PlayerDropItemEvent;
import org.bukkit.event.player.PlayerInteractEvent;
import org.bukkit.event.player.PlayerJoinEvent;
import org.bukkit.inventory.Inventory;
import org.bukkit.inventory.ItemStack;
import org.bukkit.inventory.meta.FireworkMeta;
import org.bukkit.inventory.meta.ItemMeta;
import org.bukkit.plugin.PluginManager;
import org.bukkit.plugin.java.JavaPlugin;
import org.bukkit.potion.PotionEffect;
import org.bukkit.potion.PotionEffectType;
import org.bukkit.scheduler.BukkitRunnable;
import org.bukkit.util.Vector;

public class MineplexGadgets extends JavaPlugin implements Listener {

	Server server = getServer();
	PluginManager pm = server.getPluginManager();
	public static MineplexGadgets instance = null;
	
	public MineplexGadgets getInstance() {
		return instance;
	}
	
	private Menu menu;
	
	public void onEnable() {
		pm.registerEvents(this, this);
		instance = this;
	}
	
	public void onDisable() {
		//Nothing Here :P
	}
	
	public static ItemStack createItem(Material material, int amount, boolean isEnchanted, String name, String lore) {
		ItemStack item = new ItemStack(material);
		ItemMeta meta = item.getItemMeta();
		meta.setDisplayName(name);
		item.setAmount(amount);
		ArrayList<String> Lore = new ArrayList<String>();
		Lore.add(lore);
		meta.setLore(Lore);
		if(isEnchanted) {
		meta.addEnchant(Enchantment.OXYGEN, 1, true);
		} else {
			//Do Nothing
		}
		item.setItemMeta(meta);
		
		return item;
		 
		}
	
	@EventHandler(priority=EventPriority.HIGHEST)
	public void onInventoryClick(InventoryClickEvent event) {
	Player player = (Player) event.getWhoClicked(); // The player that clicked the item
	InventoryAction action = event.getAction();
	ItemStack clicked = event.getCurrentItem(); // The item that was clicked
	Inventory inventory = event.getInventory(); // The inventory that was clicked in
	if(event.getSlot() == 4) {
		event.setCancelled(true);
	}
	if(event.getSlot() == 0) {
		if(clicked.getType() == Material.CHEST) {
		event.setCancelled(true);
		}
	}
	if (inventory.getName().equals(menu.myInventory.getName())) { // The inventory is our custom Inventory
		if(clicked.getType() != Material.AIR) {
		player.playSound(player.getLocation(), Sound.ORB_PICKUP, 10, 10);
		player.closeInventory();
		if(clicked.getType() == Material.ENDER_PEARL) {
			player.getInventory().setItem(4, createItem(Material.ENDER_PEARL, 1, true, ChatColor.GREEN + "" + ChatColor.BOLD + "Activate Ethereal Pearl", ChatColor.WHITE + "Right-click me to activate"));
		}
		if(clicked.getType() == Material.FIREWORK) {
			player.getInventory().setItem(4, createItem(Material.FIREWORK, 1, false, ChatColor.GREEN + "" + ChatColor.BOLD + "Activate Fireworks", ChatColor.WHITE + "Right-click me to activate"));
		}
		if(clicked.getType() == Material.TNT) {
			player.getInventory().setItem(4, createItem(Material.TNT, 1, false, ChatColor.GREEN + "" + ChatColor.BOLD + "Activate TNT", ChatColor.WHITE + "Right-click me to activate"));
		}
		if(clicked.getType() == Material.MELON_BLOCK) {
			player.getInventory().setItem(4, createItem(Material.MELON_BLOCK, 1, false, ChatColor.GREEN + "" + ChatColor.BOLD + "Activate Melon Launcher", ChatColor.WHITE + "Right-click me to activate"));
		}
		if(clicked.getType() == Material.GOLD_BARDING) {
			player.getInventory().setItem(4, createItem(Material.GOLD_BARDING, 1, false, ChatColor.GREEN + "" + ChatColor.BOLD + "Activate Paintball Gun", ChatColor.WHITE + "Right-click me to activate"));
		}
		if(clicked.getType() == Material.TRIPWIRE_HOOK) {
			player.getInventory().setItem(4, createItem(Material.TRIPWIRE_HOOK, 1, false, ChatColor.GREEN + "" + ChatColor.BOLD + "Activate Flesh Hook", ChatColor.WHITE + "Right-click me to activate"));
		}
		if(clicked.getType() == Material.IRON_BARDING) {
			player.getInventory().setItem(4, createItem(Material.IRON_BARDING, 1, false, ChatColor.GREEN + "" + ChatColor.BOLD + "Activate Bat Blaster", ChatColor.WHITE + "Right-click me to activate"));
		}
		if(clicked.getType() == Material.YELLOW_FLOWER) {
			player.getInventory().setItem(4, createItem(Material.YELLOW_FLOWER, 1, false, ChatColor.GREEN + "" + ChatColor.BOLD + "Activate Coin Party Bomb", ChatColor.WHITE + "Right-click me to activate"));
		}
		if(clicked.getType() == Material.INK_SACK) {
			player.playSound(player.getLocation(), Sound.DIG_WOOD, 10, 10);
			player.sendMessage(ChatColor.GOLD + "" + ChatColor.BOLD + "Gadget slot cleared!");
			player.getInventory().setItem(4, new ItemStack(Material.AIR));
		}
		event.setCancelled(true);
		} else {
			event.setCancelled(true);
		}
	}
	}
	
	@EventHandler(priority = EventPriority.HIGHEST)
	public void onEntityLand(EntityDeathEvent event) {
		Entity entity = event.getEntity();
		EntityType type = event.getEntityType();
		
		if(type == EntityType.ENDER_PEARL) {
			if(entity.getPassenger().getType() == EntityType.PLAYER) {
				Player player = (Player) entity.getPassenger();
				Firework fw = (Firework) player.getWorld().spawnEntity(player.getLocation(), EntityType.FIREWORK);
	            FireworkMeta fwm = fw.getFireworkMeta();
	           
	            FireworkEffect effect = FireworkEffect.builder().flicker(false).withColor(Color.PURPLE).withFade(Color.WHITE).with(Type.BURST).trail(false).build();
	            fwm.addEffect(effect);
	            fwm.setPower(1);
	           
	            //Then apply this to our rocket
	            fw.setFireworkMeta(fwm);      
	            player.getInventory().setItem(4, new ItemStack(Material.AIR));
			}
		}
	}
	
	@EventHandler(priority = EventPriority.HIGHEST)
	public void onItemDrop(PlayerDropItemEvent event) {
		if(event.getItemDrop().getItemStack().getItemMeta().getDisplayName().contains("Activate")) {
			event.setCancelled(true);
		}
		if(event.getItemDrop().getItemStack().getItemMeta().getDisplayName().contains("Gadgets")) {
			event.setCancelled(true);
		}
	}
	
	private Color getColor(int i) {
		Color c = null;
		if(i==1){
		c=Color.AQUA;
		}
		if(i==2){
		c=Color.BLACK;
		}
		if(i==3){
		c=Color.BLUE;
		}
		if(i==4){
		c=Color.FUCHSIA;
		}
		if(i==5){
		c=Color.GRAY;
		}
		if(i==6){
		c=Color.GREEN;
		}
		if(i==7){
		c=Color.LIME;
		}
		if(i==8){
		c=Color.MAROON;
		}
		if(i==9){
		c=Color.NAVY;
		}
		if(i==10){
		c=Color.OLIVE;
		}
		if(i==11){
		c=Color.ORANGE;
		}
		if(i==12){
		c=Color.PURPLE;
		}
		if(i==13){
		c=Color.RED;
		}
		if(i==14){
		c=Color.SILVER;
		}
		if(i==15){
		c=Color.TEAL;
		}
		if(i==16){
		c=Color.WHITE;
		}
		if(i==17){
		c=Color.YELLOW;
		}
		 
		return c;
		}
	
	@EventHandler(priority = EventPriority.HIGHEST)
	public void onPlayerPlaceBlock(PlayerInteractEvent event) {
		final Player player = event.getPlayer();
		if(event.getItem().getType() == Material.CHEST) {
			if(event.getItem().getItemMeta().getDisplayName().contains("Gadgets")) {
				server.dispatchCommand(player, "gadget");
				event.setCancelled(true);
			}
		}
		if(event.getItem().getType() == Material.ENDER_PEARL) {
			player.playSound(player.getLocation(), Sound.FIREWORK_LAUNCH, 10, 10);
			EnderPearl enderpearl = player.launchProjectile(EnderPearl.class);
			enderpearl.setPassenger(player);
			event.setCancelled(true);
			event.getPlayer().getInventory().setItem(4, new ItemStack(Material.AIR));
		}
		if(event.getItem().getType() == Material.YELLOW_FLOWER) {
			player.playSound(player.getLocation(), Sound.ITEM_PICKUP, 10, 10);
			player.sendMessage(ChatColor.RED + "" + ChatColor.BOLD + "This feature is in development. Please check back later.");
			event.setCancelled(true);
			event.getPlayer().getInventory().setItem(4, new ItemStack(Material.AIR));
		}
		if(event.getItem().getType() == Material.TNT) {
			final TNTPrimed tnt = event.getPlayer().getWorld().spawn(event.getPlayer().getLocation(), TNTPrimed.class);
			player.sendMessage(ChatColor.RED + "" + ChatColor.BOLD + "Explosion incoming!");
			player.playSound(player.getLocation(), Sound.FUSE, 10, 10);
			 new BukkitRunnable() {
				 
		            @Override
		            public void run() {
		            	Location location = tnt.getLocation();
		            	player.playSound(player.getLocation(), Sound.EXPLODE, 10, 10);
		    			double radius = 5D;
		    			List<Entity> near = player.getNearbyEntities(10.0d, 10.0d, 10.0d);
		    			for(Entity e : near) {
		    				e.setVelocity(new Vector(0, 2, 0));
		    			}
		            	tnt.remove();
		            }
		 
		        }.runTaskLater(getInstance(), 60);
			event.setCancelled(true);
			event.getPlayer().getInventory().setItem(4, new ItemStack(Material.AIR));
		}
		if(event.getItem().getType() == Material.MELON_BLOCK) {
			player.playSound(player.getLocation(), Sound.LAVA_POP, 10, 10);
			player.getWorld().dropItemNaturally(player.getLocation().add(new Vector(0, 10, 0)), createItem(Material.MELON, 64, false, ChatColor.GREEN + "" + ChatColor.BOLD + "Super Melon", ChatColor.WHITE + "Eat them to get super speed!"));
			event.setCancelled(true);
			event.getPlayer().getInventory().setItem(4, new ItemStack(Material.AIR));
		}
		if(event.getItem().getType() == Material.MELON) {
			player.playSound(player.getLocation(), Sound.ORB_PICKUP, 10, 10);
			player.sendMessage(ChatColor.GOLD + "" + ChatColor.BOLD + "* You feel different now...");
			player.addPotionEffect(new PotionEffect(PotionEffectType.SPEED, 150, 5));
			event.setCancelled(true);
			event.getPlayer().getInventory().remove(Material.MELON);
		}
		if(event.getItem().getType() == Material.GOLD_BARDING) {
			player.playSound(player.getLocation(), Sound.LAVA_POP, 10, 10);
			player.launchProjectile(Snowball.class);
			event.setCancelled(true);
		}
		if(event.getItem().getType() == Material.TRIPWIRE_HOOK) {
			player.playSound(player.getLocation(), Sound.ITEM_BREAK, 10, 10);
			player.sendMessage(ChatColor.GREEN + "" + ChatColor.BOLD + "Nearby entities have been hooked!");
			double radius = 5D;
			List<Entity> near = player.getNearbyEntities(10.0d, 10.0d, 10.0d);
			for(Entity e : near) {
				if(e.getType() == EntityType.PLAYER) {
				Player entity = (Player) e;
				player.playSound(player.getLocation(), Sound.LAVA_POP, 10, 10);
				entity.sendMessage(ChatColor.RED + "" + ChatColor.BOLD + "You have been hooked!");
				}
				e.setVelocity(new Vector(0, 3, 0));
			}
			event.setCancelled(true);
			event.getPlayer().getInventory().setItem(4, new ItemStack(Material.AIR));
		}
		if(event.getItem().getType() == Material.IRON_BARDING) {
			player.playSound(player.getLocation(), Sound.ITEM_BREAK, 10, 10);
			boolean done = false;
			if(done) {
			Bat bat = (Bat) player.getWorld().spawnEntity(player.getEyeLocation(), EntityType.BAT);
			Bat bat2 = (Bat) player.getWorld().spawnEntity(player.getEyeLocation(), EntityType.BAT);
			Bat bat3 = (Bat) player.getWorld().spawnEntity(player.getEyeLocation(), EntityType.BAT);
			Bat bat4 = (Bat) player.getWorld().spawnEntity(player.getEyeLocation(), EntityType.BAT);
			Bat bat5 = (Bat) player.getWorld().spawnEntity(player.getEyeLocation(), EntityType.BAT);
			Creature batc1 = (Creature) bat;
			Creature batc2 = (Creature) bat2;
			Creature batc3 = (Creature) bat3;
			Creature batc4 = (Creature) bat4;
			Creature batc5 = (Creature) bat5;
			double radius = 5D;
			List<Entity> near = player.getNearbyEntities(5.0d, 5.0d, 5.0d);
			for(Entity e : near) {
					batc1.setTarget((LivingEntity) e);
					batc2.setTarget((LivingEntity) e);
					batc3.setTarget((LivingEntity) e);
					batc4.setTarget((LivingEntity) e);
					batc5.setTarget((LivingEntity) e);
			}
			} else {
				player.sendMessage(ChatColor.RED + "" + ChatColor.BOLD + "This feature is in development. Please check back later.");
			}
			event.setCancelled(true);
		}
		if(event.getItem().getType() == Material.FIREWORK) {
	           //Spawn the Firework, get the FireworkMeta.
            Firework fw = (Firework) player.getWorld().spawnEntity(player.getLocation(), EntityType.FIREWORK);
            FireworkMeta fwm = fw.getFireworkMeta();
           
            //Our random generator
            Random r = new Random();   
 
            //Get the type
            int rt = r.nextInt(4) + 1;
            Type type = Type.BALL;       
            if (rt == 1) type = Type.BALL;
            if (rt == 2) type = Type.BALL_LARGE;
            if (rt == 3) type = Type.BURST;
            if (rt == 4) type = Type.CREEPER;
            if (rt == 5) type = Type.STAR;
           
            //Get our random colours   
            int r1i = r.nextInt(17) + 1;
            int r2i = r.nextInt(17) + 1;
            Color c1 = getColor(r1i);
            Color c2 = getColor(r2i);
           
            //Create our effect with this
            FireworkEffect effect = FireworkEffect.builder().flicker(r.nextBoolean()).withColor(c1).withFade(c2).with(type).trail(r.nextBoolean()).build();
           
            //Then apply the effect to the meta
            fwm.addEffect(effect);
           
            //Generate some random power and set it
            int rp = r.nextInt(2) + 1;
            fwm.setPower(rp);
           
            //Then apply this to our rocket
            fw.setFireworkMeta(fwm);
			event.setCancelled(true);
		}
	}
	
	@EventHandler(priority = EventPriority.HIGHEST)
	public void onPlayerJoin(PlayerJoinEvent event) {
		event.getPlayer().getInventory().setItem(0, createItem(Material.CHEST, 1, false, ChatColor.AQUA + "" + ChatColor.BOLD + "Gadgets", ChatColor.WHITE + "Right-click me to open the gadgets menu"));
	}
	
	@EventHandler(priority = EventPriority.HIGHEST)
	public void onEntityHit(ProjectileHitEvent event) {
		Entity entity = event.getEntity();
		EntityType type = event.getEntityType();
		
		if(type == EntityType.BAT) {
			 //Spawn the Firework, get the FireworkMeta.
	         Firework fw = (Firework) entity.getWorld().spawnEntity(entity.getLocation(), EntityType.FIREWORK);
	         FireworkMeta fwm = fw.getFireworkMeta();
	        
	         //Our random generator
	         Random r = new Random();   

	         //Get the type
	         int rt = r.nextInt(4) + 1;
	         Type type2 = Type.BALL;       
	         if (rt == 1) type2 = Type.BALL;
	         if (rt == 2) type2 = Type.BALL_LARGE;
	         if (rt == 3) type2 = Type.BURST;
	         if (rt == 4) type2 = Type.CREEPER;
	         if (rt == 5) type2 = Type.STAR;
	        
	         //Get our random colours   
	         int r1i = r.nextInt(17) + 1;
	         int r2i = r.nextInt(17) + 1;
	         Color c1 = getColor(r1i);
	         Color c2 = getColor(r2i);
	        
	         //Create our effect with this
	         FireworkEffect effect = FireworkEffect.builder().flicker(r.nextBoolean()).withColor(c1).withFade(c2).with(type2).trail(r.nextBoolean()).build();
	        
	         //Then apply the effect to the meta
	         fwm.addEffect(effect);
	        
	         //Generate some random power and set it
	         int rp = r.nextInt(2) + 1;
	         fwm.setPower(rp);
	        
	         //Then apply this to our rocket
	         fw.setFireworkMeta(fwm);
				double radius = 5D;
				List<Entity> near = entity.getNearbyEntities(3.0d, 3.0d, 3.0d);
				for(Entity e : near) {
					e.setVelocity(new Vector(0, 2, 0));
				}
	         entity.remove();
		}
		if(type == EntityType.SNOWBALL) {
	           //Spawn the Firework, get the FireworkMeta.
         Firework fw = (Firework) entity.getWorld().spawnEntity(entity.getLocation(), EntityType.FIREWORK);
         FireworkMeta fwm = fw.getFireworkMeta();
        
         //Our random generator
         Random r = new Random();   

         //Get the type
         int rt = r.nextInt(4) + 1;
         Type type2 = Type.BALL;       
         if (rt == 1) type2 = Type.BALL;
         if (rt == 2) type2 = Type.BALL_LARGE;
         if (rt == 3) type2 = Type.BURST;
         if (rt == 4) type2 = Type.CREEPER;
         if (rt == 5) type2 = Type.STAR;
        
         //Get our random colours   
         int r1i = r.nextInt(17) + 1;
         int r2i = r.nextInt(17) + 1;
         Color c1 = getColor(r1i);
         Color c2 = getColor(r2i);
        
         //Create our effect with this
         FireworkEffect effect = FireworkEffect.builder().flicker(r.nextBoolean()).withColor(c1).withFade(c2).with(type2).trail(r.nextBoolean()).build();
        
         //Then apply the effect to the meta
         fwm.addEffect(effect);
        
         //Generate some random power and set it
         int rp = r.nextInt(2) + 1;
         fwm.setPower(rp);
        
         //Then apply this to our rocket
         fw.setFireworkMeta(fwm);
		}
	}
	
	public boolean onCommand(CommandSender sender, Command command, String label, String[] args) {
		
		Player player = (Player) sender;
		
		if(label.equalsIgnoreCase("gadget")) {
			if(player.hasPermission("Gadget.Use")) {
				menu.openInventory(player);
				player.playSound(player.getLocation(), Sound.DOOR_OPEN, 10, 10);
			} else {
				player.sendMessage(ChatColor.RED + "" + ChatColor.BOLD + "You don't have permission to do that.");
				player.playSound(player.getLocation(), Sound.FIZZ, 10, 10);
			}
		}
		
		return false;
		
	}
}
